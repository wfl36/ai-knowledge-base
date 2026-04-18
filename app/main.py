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
    from app.crawler.github_trending import GitHubTrendingCrawler
    from app.agent.analyzer import ProjectAnalyzer
    from app.agent.scorer import Scorer, WeightManager
    from app.storage.writer import save_project, save_index
    from app.storage.models import ProjectInfo, ProjectWithScore, sanitize_filename
    from app.storage.version_mgr import VersionManager
    from app.review.manager import ReviewManager

    logger.info("===== Pipeline 开始 =====")

    # 1. 爬虫
    crawler = GitHubTrendingCrawler()
    raw_projects = await crawler.crawl()
    logger.info("爬虫完成，获取 %d 个 AI 项目", len(raw_projects))

    if not raw_projects:
        return {"status": "skip", "reason": "未获取到项目", "project_count": 0}

    # 2. Agent 分析 + 评分
    analyzer = ProjectAnalyzer()
    scorer = Scorer()
    review_mgr = ReviewManager()

    projects_with_scores: List[ProjectWithScore] = []
    saved_count = 0

    for raw in raw_projects:
        # 构造项目信息字符串用于 LLM 分析
        project_info_str = (
            f"项目名称: {raw.name}\n"
            f"描述: {raw.description}\n"
            f"语言: {raw.language or '未知'}\n"
            f"Stars: {raw.stars}\n"
            f"Forks: {raw.forks}\n"
            f"今日Stars: {raw.stars_today}\n"
            f"URL: {raw.url}\n"
        )

        # 调用 LLM 分析
        analysis_result = await analyzer.analyze(project_info_str)

        # 评分计算
        scored = scorer.score(analysis_result)
        logger.info(
            "项目 %s: 总分=%.2f (tech=%.1f util=%.1f comm=%.1f bonus=%.1f)",
            raw.name, scored.total_score,
            scored.tech_score, scored.utility_score, scored.community_score, scored.bonus,
        )

        # 构造 ProjectInfo
        project_info = ProjectInfo(
            name=raw.name,
            description=raw.description,
            tags=scored.tags,
            tech_stack=[raw.language] if raw.language else [],
            link=raw.url,
            date=str(date.today()),
        )

        # 将 agent.models.AnalysisResult 转换为 storage.models.AnalysisResult
        storage_analysis = _convert_analysis_result(scored)

        # 存储
        filepath = save_project(project_info, storage_analysis, KNOWLEDGE_DIR)
        saved_count += 1

        projects_with_scores.append(ProjectWithScore(
            name=raw.name,
            score=scored.total_score,
            tags=scored.tags,
            updated_at=date.today(),
            link=raw.url,
            filename=os.path.basename(filepath),
        ))

        # 判断是否需要复核
        if review_mgr.should_review(scored):
            logger.info("项目 %s 需要人工复核", raw.name)

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

    logger.info("===== Pipeline 完成 =====")
    return {
        "status": "ok",
        "project_count": len(raw_projects),
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
