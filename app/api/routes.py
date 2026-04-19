"""FastAPI 路由定义"""

import os
import logging
from typing import List, Optional

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from app.agent.models import AnalysisResult, WeightConfig
from app.agent.scorer import Scorer, WeightManager
from app.crawler.github_trending import GitHubTrendingCrawler, ProjectRaw
from app.agent.analyzer import ProjectAnalyzer
from app.storage.writer import save_project, save_index, generate_index
from app.storage.models import ProjectInfo, ProjectWithScore, sanitize_filename
from app.review.manager import ReviewManager
from app.review.models import PendingProject, ScoreSet, ReviewRecord

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# App & Templates
# ---------------------------------------------------------------------------

app = FastAPI(title="AI Knowledge Base", version="0.1.0")

_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "templates")
templates = Jinja2Templates(directory=_TEMPLATE_DIR)


# Register custom Jinja2 filters
def _basename_filter(path: str) -> str:
    return os.path.basename(path)


templates.env.filters["basename"] = _basename_filter

# ---------------------------------------------------------------------------
# Shared instances (lazily initialized)
# ---------------------------------------------------------------------------

_knowledge_dir: str = os.getenv("KNOWLEDGE_DIR", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge"))
_review_manager = ReviewManager()
_scorer = Scorer()


def _load_projects_from_knowledge() -> List[dict]:
    """递归扫描 knowledge/ 下的日期子目录，返回项目列表供渲染。"""
    import re
    from pathlib import Path
    from datetime import date

    knowledge_path = Path(_knowledge_dir)
    if not knowledge_path.exists():
        return []

    projects: List[dict] = []
    _re_title = re.compile(r"^#\s+(.+)$", re.MULTILINE)
    _re_score = re.compile(r"\*\*评分：\*\*\s*([\d.]+)", re.MULTILINE)
    _re_status = re.compile(r"\*\*状态：\*\*\s*(.+)", re.MULTILINE)
    _re_tags = re.compile(r"\*\*标签：\*\*\s*(.+)", re.MULTILINE)
    _re_date = re.compile(r"\*\*更新日期：\*\*\s*(.+)", re.MULTILINE)

    # 递归扫描所有子目录中的 .md 文件
    for md_file in sorted(knowledge_path.rglob("*.md")):
        if md_file.name == "index.md":
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        title_m = _re_title.search(content)
        score_m = _re_score.search(content)
        status_m = _re_status.search(content)
        tags_m = _re_tags.search(content)
        date_m = _re_date.search(content)

        name = title_m.group(1).strip() if title_m else md_file.stem
        score = float(score_m.group(1)) if score_m else 0.0
        status = status_m.group(1).strip() if status_m else "正常"
        tags = [t.strip() for t in tags_m.group(1).split(",")] if tags_m else []
        updated = date_m.group(1).strip() if date_m else ""

        # 相对路径: 2026-04-19/project_9.0_2026-04-19.md
        rel_path = md_file.relative_to(knowledge_path)
        # 日期目录名（如果有）
        date_dir = rel_path.parts[0] if len(rel_path.parts) > 1 else ""

        projects.append({
            "name": name,
            "rel_path": str(rel_path),
            "filename": md_file.name,
            "date_dir": date_dir,
            "score": score,
            "status": status,
            "tags": tags,
            "updated_at": updated,
        })

    projects.sort(key=lambda p: p["score"], reverse=True)
    return projects


# ===========================================================================
# HTML Routes
# ===========================================================================

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """首页 — 展示知识库总纲"""
    projects = _load_projects_from_knowledge()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "projects": projects,
    })


@app.get("/projects/{date_dir}/{filename}", response_class=HTMLResponse)
async def project_detail(request: Request, date_dir: str, filename: str):
    """查看单个项目详情（日期子目录）"""
    from pathlib import Path
    import re

    filepath = Path(_knowledge_dir) / date_dir / filename
    if not filepath.exists():
        return HTMLResponse("<h1>404 - 项目未找到</h1>", status_code=404)

    content = filepath.read_text(encoding="utf-8")

    # Parse key fields for template use
    _re_title = re.compile(r"^#\s+(.+)$", re.MULTILINE)
    _re_score = re.compile(r"\*\*评分：\*\*\s*([\d.]+)", re.MULTILINE)
    _re_status = re.compile(r"\*\*状态：\*\*\s*(.+)", re.MULTILINE)
    _re_tags = re.compile(r"\*\*标签：\*\*\s*(.+)", re.MULTILINE)
    _re_date = re.compile(r"\*\*更新日期：\*\*\s*(.+)", re.MULTILINE)

    title_m = _re_title.search(content)
    score_m = _re_score.search(content)
    status_m = _re_status.search(content)
    tags_m = _re_tags.search(content)
    date_m = _re_date.search(content)

    project = {
        "name": title_m.group(1).strip() if title_m else filename,
        "filename": filename,
        "date_dir": date_dir,
        "score": float(score_m.group(1)) if score_m else 0.0,
        "status": status_m.group(1).strip() if status_m else "正常",
        "tags": [t.strip() for t in tags_m.group(1).split(",")] if tags_m else [],
        "updated_at": date_m.group(1).strip() if date_m else "",
        "content": content,
    }

    return templates.TemplateResponse("project.html", {
        "request": request,
        "project": project,
    })


@app.get("/review", response_class=HTMLResponse)
async def review_page(request: Request):
    """审核页面 — 展示待复核项目列表"""
    pending = ReviewManager.load_pending(_knowledge_dir)
    return templates.TemplateResponse("review.html", {
        "request": request,
        "pending_projects": pending,
    })


@app.post("/review/{project_name}")
async def submit_review(
    request: Request,
    project_name: str,
    reviewer: str = Form(...),
    tech_score: float = Form(...),
    utility_score: float = Form(...),
    community_score: float = Form(...),
    reason: str = Form(...),
):
    """提交复核"""
    modified = ScoreSet(tech=tech_score, utility=utility_score, community=community_score)
    record = _review_manager.submit_review(
        project_name=project_name,
        reviewer=reviewer,
        modified_scores=modified,
        reason=reason,
    )
    _review_manager.approve_review(record)
    return JSONResponse({"status": "ok", "message": f"复核已提交: {project_name}"})


# ===========================================================================
# JSON API Routes
# ===========================================================================

@app.get("/api/projects")
async def api_projects():
    """JSON API — 获取所有项目"""
    projects = _load_projects_from_knowledge()
    return JSONResponse(projects)


@app.get("/api/weights")
async def api_weights():
    """获取当前权重配置"""
    wc = _scorer.weight_config
    return JSONResponse(wc.model_dump())


@app.post("/api/crawl")
async def api_crawl():
    """手动触发一次抓取+分析"""
    try:
        from app.main import run_pipeline
        result = await run_pipeline()
        return JSONResponse({"status": "ok", "message": "抓取+分析完成", "detail": result})
    except Exception as exc:
        logger.exception("手动抓取失败")
        return JSONResponse({"status": "error", "message": str(exc)}, status_code=500)


@app.post("/api/adjust-weights")
async def api_adjust_weights():
    """手动触发权重调整"""
    changed = _scorer.adjust_weights()
    return JSONResponse({
        "status": "ok",
        "changed": changed,
        "weights": _scorer.weight_config.model_dump(),
    })
