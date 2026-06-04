"""通用资源模型 Item

所有信息源(GitHub / RSS / Hacker News ...)抓取后统一产出 Item，
供 pipeline 做统一的分析、评分与存储。
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    """跨来源的统一资源条目"""

    source_type: str = Field(..., description="来源类型: github | rss | hackernews")
    title: str = Field(..., description="标题(GitHub 为 owner/repo, 文章为标题)")
    url: str = Field(..., description="资源链接(必有, 供 markdown 链接区使用)")
    summary: str = Field(default="", description="摘要/描述")
    author: Optional[str] = Field(default=None, description="作者")
    published_at: Optional[datetime] = Field(default=None, description="发布时间")
    language: Optional[str] = Field(default=None, description="编程语言(仅项目类)")
    metrics: dict = Field(default_factory=dict, description="来源相关指标")
    raw_text: Optional[str] = Field(default=None, description="可选全文")

    def to_info_str(self) -> str:
        """构造喂给 LLM 的信息文本，按来源类型补充相关指标。

        替代原 app/main.py 的 _build_info_str。
        """
        lines = [f"标题: {self.title}"]
        if self.summary:
            lines.append(f"摘要: {self.summary}")
        if self.author:
            lines.append(f"作者: {self.author}")
        if self.published_at:
            lines.append(f"发布时间: {self.published_at.date()}")

        if self.source_type == "github":
            m = self.metrics
            lines.append(f"语言: {self.language or '未知'}")
            lines.append(f"Stars: {m.get('stars', 0)}")
            lines.append(f"Forks: {m.get('forks', 0)}")
            lines.append(f"今日Stars: {m.get('stars_today', 0)}")
        elif self.source_type == "hackernews":
            m = self.metrics
            lines.append(f"HN Points: {m.get('points', 0)}")
            lines.append(f"HN 评论数: {m.get('num_comments', 0)}")

        if self.raw_text:
            # 控制长度，避免超长正文撑爆 prompt
            lines.append(f"正文节选: {self.raw_text[:2000]}")

        lines.append(f"URL: {self.url}")
        return "\n".join(lines)
