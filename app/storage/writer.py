"""知识条目 Markdown 生成与持久化"""

import os
from datetime import date
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
# 文件保存
# ---------------------------------------------------------------------------

def save_project(project_info: ProjectInfo, analysis: AnalysisResult, knowledge_dir: str) -> str:
    """保存单个项目 Markdown 文件，返回文件路径"""

    os.makedirs(knowledge_dir, exist_ok=True)
    content = generate_project_md(project_info, analysis)
    filename = _project_filename(project_info, analysis)
    filepath = os.path.join(knowledge_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def save_index(projects: List[ProjectInfo], knowledge_dir: str,
               analysis_map: dict = None) -> str:
    """保存总纲 index.md

    Args:
        projects: 项目信息列表
        knowledge_dir: 知识库目录
        analysis_map: 可选的 {project_name: AnalysisResult} 映射
    """

    os.makedirs(knowledge_dir, exist_ok=True)

    scored_projects = []
    for p in projects:
        analysis = analysis_map.get(p.name) if analysis_map else None
        score = analysis.total_score if analysis else 0.0
        tags = analysis.tags if analysis else p.tags
        updated = date.fromisoformat(p.date) if isinstance(p.date, str) else p.date
        scored_projects.append(ProjectWithScore(
            name=p.name,
            score=score,
            tags=tags,
            updated_at=updated,
            link=p.link,
        ))

    content = generate_index(scored_projects)
    filepath = os.path.join(knowledge_dir, "index.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath
