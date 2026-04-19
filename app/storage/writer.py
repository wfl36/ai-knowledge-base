"""知识条目 Markdown 生成与持久化"""

import os
import shutil
from datetime import date, timedelta
from typing import List

from .models import AnalysisResult, ProjectInfo, ProjectWithScore, sanitize_filename

# ---------------------------------------------------------------------------
# Markdown 生成
# ---------------------------------------------------------------------------

def generate_project_md(project_info: ProjectInfo, analysis: AnalysisResult) -> str:
    """按模板生成单个项目的 Markdown 内容"""

    tags_str = ", ".join(analysis.tags) if analysis.tags else "无"
    tech_stack_str = "\n".join(f"- {t}" for t in project_info.tech_stack) if project_info.tech_stack else "- 未标注"

    return f"""# {project_info.name}

**评分：** {analysis.total_score:.1f}  
**状态：** {analysis.status.value}  
**标签：** {tags_str}  
**更新日期：** {project_info.date}  

## 项目描述
{project_info.description}

## 技术栈
{tech_stack_str}

## 分析摘要
### 技术先进性 (评分: {analysis.tech_score:.1f}/10)
{analysis.tech_summary}

### 实用性 (评分: {analysis.utility_score:.1f}/10)
{analysis.utility_summary}

### 社区活跃度 (评分: {analysis.community_score:.1f}/10)
{analysis.community_summary}

## 项目链接
{project_info.link}
"""


def generate_index(projects: List[ProjectWithScore]) -> str:
    """生成总纲 Markdown，按评分降序排列"""

    sorted_projects = sorted(projects, key=lambda p: p.score, reverse=True)

    lines = [
        "# AI 知识库总纲",
        "",
        f"> 最后更新: {date.today().isoformat()}",
        f"> 项目总数: {len(sorted_projects)}",
        "",
        "| # | 项目名称 | 评分 | 标签 | 状态 | 更新日期 | 链接 |",
        "|---|---------|------|------|------|---------|------|",
    ]

    for i, p in enumerate(sorted_projects, 1):
        tags_str = ", ".join(p.tags[:3]) if p.tags else "-"
        lines.append(
            f"| {i} | {p.name} | {p.score:.1f} | {tags_str} | "
            f"{'待复核' if p.score < 6 else '正常'} | {p.updated_at} | [链接]({p.link}) |"
        )

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 文件名生成
# ---------------------------------------------------------------------------

def _project_filename(project_info: ProjectInfo, analysis: AnalysisResult) -> str:
    safe_name = sanitize_filename(project_info.name)
    return f"{safe_name}_{analysis.total_score:.1f}_{project_info.date}.md"


# ---------------------------------------------------------------------------
# 日期子目录
# ---------------------------------------------------------------------------

def _date_dir(knowledge_dir: str, d: date = None) -> str:
    """返回日期子目录路径: knowledge/2026-04-19/"""
    day = d or date.today()
    return os.path.join(knowledge_dir, day.isoformat())


# ---------------------------------------------------------------------------
# 文件保存
# ---------------------------------------------------------------------------

def save_project(project_info: ProjectInfo, analysis: AnalysisResult, knowledge_dir: str) -> str:
    """保存单个项目 Markdown 文件到日期子目录，返回文件路径"""

    day_dir = _date_dir(knowledge_dir)
    os.makedirs(day_dir, exist_ok=True)

    content = generate_project_md(project_info, analysis)
    filename = _project_filename(project_info, analysis)
    filepath = os.path.join(day_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def save_index(projects: List[ProjectWithScore], knowledge_dir: str) -> str:
    """保存总纲 index.md（在 knowledge 根目录）"""

    os.makedirs(knowledge_dir, exist_ok=True)

    content = generate_index(projects)
    filepath = os.path.join(knowledge_dir, "index.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


# ---------------------------------------------------------------------------
# 清理过期目录
# ---------------------------------------------------------------------------

def cleanup_old_dirs(knowledge_dir: str, keep_days: int = 30) -> List[str]:
    """清理超过 keep_days 天的日期子目录，返回被删除的目录名列表。

    只删除符合 YYYY-MM-DD 格式的子目录，不会删除 index.md 等根目录文件。
    """
    if not os.path.isdir(knowledge_dir):
        return []

    cutoff = date.today() - timedelta(days=keep_days)
    removed: List[str] = []

    for entry in sorted(os.listdir(knowledge_dir)):
        full_path = os.path.join(knowledge_dir, entry)
        if not os.path.isdir(full_path):
            continue
        # 只处理 YYYY-MM-DD 格式的目录
        try:
            dir_date = date.fromisoformat(entry)
        except ValueError:
            continue
        if dir_date < cutoff:
            shutil.rmtree(full_path, ignore_errors=True)
            removed.append(entry)

    return removed
