"""复核模块数据模型 (Pydantic v2)"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ReviewStatus(str, Enum):
    """复核状态"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class ScoreSet(BaseModel):
    """三维评分集合"""
    tech: float = Field(..., ge=0.0, le=10.0, description="技术先进性评分")
    utility: float = Field(..., ge=0.0, le=10.0, description="实用性评分")
    community: float = Field(..., ge=0.0, le=10.0, description="社区活跃度评分")


class ReviewRecord(BaseModel):
    """人工复核记录"""
    project_name: str = Field(..., description="项目名称")
    review_time: datetime = Field(default_factory=datetime.now, description="复核时间")
    reviewer: str = Field(..., description="复核人员")
    original_scores: ScoreSet = Field(..., description="原始评分")
    modified_scores: ScoreSet = Field(..., description="修改后评分")
    reason: str = Field(..., description="修改原因")
    status: ReviewStatus = Field(default=ReviewStatus.PENDING, description="复核状态")


class PendingProject(BaseModel):
    """待复核项目（从 Markdown 解析而来）"""
    project_name: str = Field(..., description="项目名称")
    file_path: str = Field(..., description="Markdown 文件路径")
    score: float = Field(default=0.0, description="当前总评分")
    status_text: str = Field(default="待复核", description="状态文本")


class CompressedHistory(BaseModel):
    """压缩后的历史摘要（按月聚合）"""
    month: str = Field(..., description="月份，格式 YYYY-MM")
    record_count: int = Field(default=0, description="记录数量")
    avg_tech_diff: float = Field(default=0.0, description="技术先进性平均偏差")
    avg_utility_diff: float = Field(default=0.0, description="实用性平均偏差")
    avg_community_diff: float = Field(default=0.0, description="社区活跃度平均偏差")
    approved_count: int = Field(default=0, description="通过数量")
    rejected_count: int = Field(default=0, description="驳回数量")
    summary: str = Field(default="", description="压缩摘要")
