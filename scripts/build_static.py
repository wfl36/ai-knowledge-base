#!/usr/bin/env python3
"""将 knowledge/ 下的 markdown 文件转为 JSON，供静态前端使用"""

import json
import os
import re
import sys
from pathlib import Path


def parse_project_md(filepath: Path, knowledge_dir: Path) -> dict | None:
    """解析单个项目 markdown 文件，返回结构化数据"""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    # 提取各字段
    title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    score_m = re.search(r"\*\*评分：\*\*\s*([\d.]+)", content)
    status_m = re.search(r"\*\*状态：\*\*\s*(.+)", content)
    tags_m = re.search(r"\*\*标签：\*\*\s*(.+)", content)
    date_m = re.search(r"\*\*更新日期：\*\*\s*(.+)", content)
    # 来源(附加字段，老文件无此行时默认 github)
    source_m = re.search(r"\*\*来源：\*\*\s*(.+)", content)

    # 提取项目描述(限定在本段内，不跨越下一个 ## 标题；空描述返回 "")
    desc_m = re.search(r"## 项目描述\n(.*?)(?=\n## )", content, re.DOTALL)
    description = desc_m.group(1).strip() if desc_m else ""

    # 提取综合总结(LLM 生成的综合摘要)
    summary_m = re.search(r"## 综合总结\n(.*?)(?=\n## )", content, re.DOTALL)
    summary = summary_m.group(1).strip() if summary_m else ""
    if summary == "无":
        summary = ""

    # 提取技术栈
    tech_m = re.search(r"## 技术栈\n+((?:- .+\n?)+)", content)
    tech_stack = []
    if tech_m:
        tech_stack = [t.strip("- ") for t in tech_m.group(1).strip().split("\n") if t.strip()]

    # 提取分析摘要
    tech_adv_m = re.search(r"### 技术先进性 \(评分: ([\d.]+)/10\)\n+(.+?)(?=\n###|\n##|\Z)", content, re.DOTALL)
    utility_m = re.search(r"### 实用性 \(评分: ([\d.]+)/10\)\n+(.+?)(?=\n###|\n##|\Z)", content, re.DOTALL)
    community_m = re.search(r"### 社区活跃度 \(评分: ([\d.]+)/10\)\n+(.+?)(?=\n###|\n##|\Z)", content, re.DOTALL)

    # 提取项目链接
    link_m = re.search(r"## 项目链接\n+(https?://.+)", content)

    # 日期目录
    rel_path = filepath.relative_to(knowledge_dir)
    date_dir = rel_path.parts[0] if len(rel_path.parts) > 1 else ""

    name = title_m.group(1).strip() if title_m else filepath.stem
    tags = [t.strip() for t in tags_m.group(1).split(",")] if tags_m else []

    return {
        "name": name,
        "score": float(score_m.group(1)) if score_m else 0.0,
        "status": status_m.group(1).strip() if status_m else "正常",
        "tags": tags,
        "date": date_m.group(1).strip() if date_m else "",
        "date_dir": date_dir,
        "filename": filepath.name,
        "source_type": source_m.group(1).strip() if source_m else "github",
        "description": description,
        "summary": summary,
        "tech_stack": tech_stack,
        "link": link_m.group(1).strip() if link_m else "",
        "analysis": {
            "tech": {
                "score": float(tech_adv_m.group(1)) if tech_adv_m else 0.0,
                "summary": tech_adv_m.group(2).strip() if tech_adv_m else "",
            },
            "utility": {
                "score": float(utility_m.group(1)) if utility_m else 0.0,
                "summary": utility_m.group(2).strip() if utility_m else "",
            },
            "community": {
                "score": float(community_m.group(1)) if community_m else 0.0,
                "summary": community_m.group(2).strip() if community_m else "",
            },
        },
    }


def build(knowledge_dir: str, output_dir: str):
    """扫描 knowledge 目录，生成 JSON 数据"""
    kpath = Path(knowledge_dir)
    if not kpath.exists():
        print(f"Knowledge directory not found: {kpath}")
        sys.exit(1)

    # 收集所有日期目录
    dates = sorted(
        [d.name for d in kpath.iterdir() if d.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", d.name)],
        reverse=True,
    )

    # 解析所有项目
    all_projects = []
    projects_by_date = {}

    for date_dir_name in dates:
        date_path = kpath / date_dir_name
        date_projects = []

        for md_file in sorted(date_path.glob("*.md")):
            project = parse_project_md(md_file, kpath)
            if project:
                date_projects.append(project)
                all_projects.append(project)

        projects_by_date[date_dir_name] = date_projects

    # 去重：同名项目只保留最新
    seen = {}
    for p in all_projects:
        name = p["name"]
        if name not in seen or p["date"] > seen[name]["date"]:
            seen[name] = p

    unique_projects = sorted(seen.values(), key=lambda x: x["score"], reverse=True)

    # 生成统计
    all_tags = {}
    for p in unique_projects:
        for tag in p["tags"]:
            all_tags[tag] = all_tags.get(tag, 0) + 1

    top_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:20]

    # 按来源统计(供前端来源过滤)
    source_counts = {}
    for p in unique_projects:
        st = p.get("source_type", "github")
        source_counts[st] = source_counts.get(st, 0) + 1

    data = {
        "last_updated": dates[0] if dates else "",
        "total_projects": len(unique_projects),
        "total_dates": len(dates),
        "dates": dates,
        "top_tags": [{"name": t, "count": c} for t, c in top_tags],
        "sources": [{"name": s, "count": c} for s, c in sorted(source_counts.items(), key=lambda x: x[1], reverse=True)],
        "projects": unique_projects,
        "projects_by_date": {k: [p["name"] for p in v] for k, v in projects_by_date.items()},
    }

    # 输出
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    json_path = out_path / "data.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Generated {json_path}: {len(unique_projects)} projects, {len(dates)} dates")
    return data


if __name__ == "__main__":
    knowledge_dir = sys.argv[1] if len(sys.argv) > 1 else "./knowledge"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./site/data"
    build(knowledge_dir, output_dir)
