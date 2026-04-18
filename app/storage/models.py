"""Pydantic models for knowledge base storage."""

from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ProjectStatus(str, Enum):
    NORMAL = "正常"
    PENDING_REVIEW = "待复核"
    FAILED = "分析失败"


class ProjectInfo(BaseModel):
    """Basic project information from crawling."""

    name: str = Field(..., description="项目名称")
    description: str = Field(default="", description="项目描述")
    tags: List[str] = Field(default_factory=list, description="标签列表")
    tech_stack: List[str] = Field(default_factory=list, description="技术栈")
    link: str = Field(default="", description="项目链接")
    date: str = Field(default_factory=lambda: str(date.today()), description="更新日期")


class AnalysisResult(BaseModel):
    """Analysis result from AI evaluation - matches app.agent.models.AnalysisResult."""

    tech_score: float = Field(default=0.0, ge=0, le=10, description="技术先进性 1-10")
    utility_score: float = Field(default=0.0, ge=0, le=10, description="实用性 1-10")
    community_score: float = Field(default=0.0, ge=0, le=10, description="社区活跃度 1-10")
    total_score: float = Field(default=0.0, ge=0, le=12, description="加权总分 (含加分)")
    bonus: float = Field(default=0.0, ge=0, le=2, description="特别加分")
    status: ProjectStatus = Field(default=ProjectStatus.NORMAL, description="状态")
    tags: List[str] = Field(default_factory=list, description="标签列表")
    summary: str = Field(default="", description="综合摘要")
    tech_summary: str = Field(default="", description="技术先进性摘要")
    utility_summary: str = Field(default="", description="实用性摘要")
    community_summary: str = Field(default="", description="社区活跃度摘要")


class ProjectWithScore(BaseModel):
    """Project combined with its score, used for index generation."""

    name: str
    score: float
    tags: List[str]
    updated_at: date
    link: str = Field(default="")
    filename: str = Field(default="", description="项目文件名(含.md后缀)")

    def model_post_init(self, __context) -> None:
        if not self.filename:
            safe_name = sanitize_filename(self.name)
            self.filename = f"{safe_name}_{self.score:.1f}_{self.updated_at.isoformat()}.md"


class VersionInfo(BaseModel):
    """Version snapshot metadata."""

    id: str = Field(..., description="版本ID (时间戳)")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    file_count: int = Field(default=0, description="文件数量")


class DiffResult(BaseModel):
    """Result of comparing two versions."""

    version_a: str
    version_b: str
    added: List[str] = Field(default_factory=list, description="新增文件")
    removed: List[str] = Field(default_factory=list, description="删除文件")
    modified: List[str] = Field(default_factory=list, description="修改文件")


def sanitize_filename(name: str) -> str:
    """将项目名中的特殊字符替换为 -"""
    import re
    return re.sub(r"[^\w\-.]", "-", name).strip("-")
