"""AI Knowledge Base 主入口

- APScheduler 定时任务
- run_pipeline 协调完整流程
- CLI 子命令: serve / crawl / adjust-weights
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import sys
from datetime import date
from typing import List

from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# 加载 .env (最先执行)
# override=False: 环境变量优先于 .env 文件，避免 CI 环境变量被覆盖
# ---------------------------------------------------------------------------
load_dotenv(override=False)

# ---------------------------------------------------------------------------
# 日志配置
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 环境变量
# ---------------------------------------------------------------------------
KNOWLEDGE_DIR = os.getenv("KNOWLEDGE_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "knowledge"))
VERSIONS_DIR = os.getenv("VERSIONS_DIR", os.path.join(KNOWLEDGE_DIR, "..", "versions"))
CRAWL_SCHEDULE = os.getenv("CRAWL_SCHEDULE", "0 0 * * *")  # 默认每天 0 点
LLM_CONCURRENCY = int(os.getenv("LLM_CONCURRENCY", "5"))  # LLM 分析并发数
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))


# ===========================================================================
# Pipeline
# ===========================================================================

async def run_pipeline() -> dict:
    """协调 爬虫 → Agent分析 → 评分 → 存储 → 版本快照 的完整流程

    Returns:
        dict 包含本次执行结果的摘要
    """
    import httpx

    from app.sources import build_sources
    from app.agent.analyzer import ProjectAnalyzer
    from app.agent.scorer import Scorer
    from app.storage.writer import save_project, save_index, cleanup_old_dirs
    from app.storage.models import ProjectInfo, ProjectWithScore
    from app.storage.version_mgr import VersionManager
    from app.review.manager import ReviewManager

    logger.info("===== Pipeline 开始 =====")

    # 1. 多源抓取（各源并发，单源失败不影响其余源）
    sources = build_sources()
    if not sources:
        return {"status": "skip", "reason": "未启用任何信息源", "project_count": 0}
    logger.info("启用信息源: %s", ", ".join(s.source_type for s in sources))

    fetch_results = await asyncio.gather(
        *(s.fetch() for s in sources), return_exceptions=True
    )
    items = []
    for src, result in zip(sources, fetch_results):
        if isinstance(result, Exception):
            logger.error("信息源 %s 抓取失败: %s", src.source_type, result)
            continue
        logger.info("信息源 %s 获取 %d 条", src.source_type, len(result))
        items.extend(result)

    # 跨源按归一化 URL 去重（首见保留）
    seen_urls: set = set()
    deduped = []
    for it in items:
        key = it.url.rstrip("/").lower()
        if key in seen_urls:
            continue
        seen_urls.add(key)
        deduped.append(it)
    items = deduped
    logger.info("合并去重后共 %d 条资源", len(items))

    if not items:
        return {"status": "skip", "reason": "未获取到资源", "project_count": 0}

    # 2. Agent 分析 + 评分
    analyzer = ProjectAnalyzer()
    scorer = Scorer()
    review_mgr = ReviewManager()

    projects_with_scores: List[ProjectWithScore] = []
    saved_count = 0

    # 并发调用 LLM 分析（仅网络部分并发，文件写入仍按原顺序串行）。
    # 用信号量限制并发量，避免触发 API 限流；共享一个 httpx 客户端复用连接。
    sem = asyncio.Semaphore(LLM_CONCURRENCY)

    async def _analyze_one(item, client):
        async with sem:
            return await analyzer.analyze(
                item.to_info_str(), client=client, source_type=item.source_type
            )

    async with httpx.AsyncClient(timeout=120.0, http2=False) as llm_client:
        analysis_results = await asyncio.gather(
            *(_analyze_one(item, llm_client) for item in items)
        )

    # 评分 + 存储（按原顺序串行，保证文件写入与索引稳定）
    for item, analysis_result in zip(items, analysis_results):
        # 评分计算
        scored = scorer.score(analysis_result)
        logger.info(
            "[%s] %s: 总分=%.2f (tech=%.1f util=%.1f comm=%.1f bonus=%.1f)",
            item.source_type, item.title, scored.total_score,
            scored.tech_score, scored.utility_score, scored.community_score, scored.bonus,
        )

        # 构造 ProjectInfo
        project_info = ProjectInfo(
            name=item.title,
            description=item.summary,
            tags=scored.tags,
            tech_stack=[item.language] if item.language else [],
            link=item.url,
            date=str(date.today()),
        )

        # 将 agent.models.AnalysisResult 转换为 storage.models.AnalysisResult
        storage_analysis = _convert_analysis_result(scored)

        # 存储
        filepath = save_project(
            project_info, storage_analysis, KNOWLEDGE_DIR, source_type=item.source_type
        )
        saved_count += 1

        projects_with_scores.append(ProjectWithScore(
            name=item.title,
            score=scored.total_score,
            tags=scored.tags,
            updated_at=date.today(),
            link=item.url,
            filename=os.path.basename(filepath),
        ))

        # 判断是否需要复核
        if review_mgr.should_review(scored):
            logger.info("资源 %s 需要人工复核", item.title)

    # 3. 生成总纲
    index_path = save_index(projects_with_scores, KNOWLEDGE_DIR)
    logger.info("总纲已保存: %s", index_path)

    # 4. 版本快照
    try:
        version_mgr = VersionManager()
        version_info = version_mgr.snapshot(KNOWLEDGE_DIR, VERSIONS_DIR)
        logger.info("版本快照已创建: %s", version_info.version_id)
        # 保留最近 5 个版本
        removed = version_mgr.keep_last_n(VERSIONS_DIR, n=5)
        if removed:
            logger.info("已清理旧版本: %s", removed)
    except FileExistsError:
        logger.warning("版本快照已存在，跳过")
    except Exception as exc:
        logger.error("版本快照失败: %s", exc)

    # 5. 清理过期目录
    try:
        removed_dirs = cleanup_old_dirs(KNOWLEDGE_DIR, keep_days=15)
        if removed_dirs:
            logger.info("已清理 %d 个过期目录: %s", len(removed_dirs), removed_dirs)
    except Exception as exc:
        logger.error("清理过期目录失败: %s", exc)

    logger.info("===== Pipeline 完成 =====")
    return {
        "status": "ok",
        "project_count": len(items),
        "saved_count": saved_count,
    }


def _convert_analysis_result(agent_result) -> "app.storage.models.AnalysisResult":
    """将 app.agent.models.AnalysisResult 转换为 app.storage.models.AnalysisResult"""
    from app.storage.models import AnalysisResult as StorageAnalysisResult
    from app.storage.models import ProjectStatus

    status_map = {
        "正常": ProjectStatus.NORMAL,
        "待复核": ProjectStatus.PENDING_REVIEW,
    }
    status_text = agent_result.status.value if hasattr(agent_result.status, "value") else str(agent_result.status)
    storage_status = status_map.get(status_text, ProjectStatus.NORMAL)
    if agent_result.total_score < 6:
        storage_status = ProjectStatus.PENDING_REVIEW

    return StorageAnalysisResult(
        tech_score=agent_result.tech_score,
        utility_score=agent_result.utility_score,
        community_score=agent_result.community_score,
        total_score=agent_result.total_score,
        bonus=agent_result.bonus,
        status=storage_status,
        tags=agent_result.tags,
        summary=agent_result.summary or "",
        tech_summary=agent_result.tech_summary or "",
        utility_summary=agent_result.utility_summary or "",
        community_summary=agent_result.community_summary or "",
    )


# ===========================================================================
# Scheduler
# ===========================================================================

def _start_scheduler():
    """启动 APScheduler 定时任务"""
    try:
        from apscheduler.schedulers.asyncio import AsyncIOScheduler
        from apscheduler.triggers.cron import CronTrigger
    except ImportError:
        logger.error("apscheduler 未安装，请运行: pip install apscheduler")
        return None

    scheduler = AsyncIOScheduler()

    # 解析 CRAWL_SCHEDULE cron 表达式
    parts = CRAWL_SCHEDULE.strip().split()
    if len(parts) == 5:
        trigger = CronTrigger(
            minute=parts[0],
            hour=parts[1],
            day=parts[2],
            month=parts[3],
            day_of_week=parts[4],
        )
    else:
        logger.warning("CRAWL_SCHEDULE 格式不正确，使用默认值 '0 0 * * *'")
        trigger = CronTrigger(hour=0, minute=0)

    scheduler.add_job(
        _run_pipeline_sync,
        trigger=trigger,
        id="pipeline_job",
        name="AI Knowledge Base Pipeline",
        replace_existing=True,
    )

    return scheduler


def _run_pipeline_sync():
    """同步包装器，用于 APScheduler 调用"""
    try:
        asyncio.run(run_pipeline())
    except Exception as exc:
        logger.exception("Pipeline 执行失败: %s", exc)


# ===========================================================================
# CLI
# ===========================================================================

def cli():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(
        prog="ai-kb",
        description="AI Knowledge Base 管理工具",
    )
    subparsers = parser.add_subparsers(dest="command", help="可用子命令")

    # --- serve ---
    serve_parser = subparsers.add_parser("serve", help="启动 API 服务")
    serve_parser.add_argument("--host", default=API_HOST, help="监听地址")
    serve_parser.add_argument("--port", type=int, default=API_PORT, help="监听端口")
    serve_parser.add_argument("--reload", action="store_true", help="开发模式热重载")
    serve_parser.add_argument("--no-scheduler", action="store_true", help="不启动定时任务")

    # --- crawl ---
    crawl_parser = subparsers.add_parser("crawl", help="执行一次抓取+分析")
    crawl_parser.add_argument("--knowledge-dir", default=KNOWLEDGE_DIR, help="知识库目录")

    # --- adjust-weights ---
    adjust_parser = subparsers.add_parser("adjust-weights", help="触发权重调整")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    if args.command == "serve":
        _cmd_serve(args)
    elif args.command == "crawl":
        _cmd_crawl(args)
    elif args.command == "adjust-weights":
        _cmd_adjust_weights(args)
    else:
        parser.print_help()


def _cmd_serve(args):
    """启动 API 服务"""
    import uvicorn
    from app.api.routes import app

    # 启动定时任务
    if not args.no_scheduler:
        scheduler = _start_scheduler()
        if scheduler:
            scheduler.start()
            logger.info("定时任务已启动 (cron: %s)", CRAWL_SCHEDULE)

    logger.info("启动 API 服务: %s:%d", args.host, args.port)
    uvicorn.run(
        "app.api.routes:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


def _cmd_crawl(args):
    """执行一次抓取"""
    global KNOWLEDGE_DIR
    if args.knowledge_dir:
        KNOWLEDGE_DIR = args.knowledge_dir
    result = asyncio.run(run_pipeline())
    print(json.dumps(result, ensure_ascii=False, indent=2))


def _cmd_adjust_weights(args):
    """触发权重调整"""
    from app.agent.scorer import Scorer
    scorer = Scorer()
    changed = scorer.adjust_weights()
    wc = scorer.weight_config
    if changed:
        print(f"权重已调整: tech={wc.tech_weight:.4f} utility={wc.utility_weight:.4f} community={wc.community_weight:.4f}")
    else:
        print(f"权重未变化: tech={wc.tech_weight:.4f} utility={wc.utility_weight:.4f} community={wc.community_weight:.4f}")


# ===========================================================================
# Entry Point
# ===========================================================================

if __name__ == "__main__":
    cli()
