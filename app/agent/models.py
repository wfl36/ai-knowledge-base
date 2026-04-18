"""Pydantic 数据模型"""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, model_validator


class AnalysisStatus(str, Enum):
    """分析结果状态"""
    NORMAL = "正常"
    PENDING_REVIEW = "待复核"
    FAILED = "分析失败"


class WeightConfig(BaseModel):
    """权重配置"""
    tech_weight: float = Field(default=1 / 3, ge=0.2, le=0.5, description="技术先进性权重")
    utility_weight: float = Field(default=1 / 3, ge=0.2, le=0.5, description="实用性权重")
    community_weight: float = Field(default=1 / 3, ge=0.2, le=0.5, description="社区活跃度权重")

    @model_validator(mode="after")
    def weights_sum_to_one(self) -> "WeightConfig":
        total = self.tech_weight + self.utility_weight + self.community_weight
        if abs(total - 1.0) > 0.01:
            raise ValueError(f"权重之和必须为 1.0，当前为 {total:.4f}")
        return self


class AnalysisResult(BaseModel):
    """分析评分结果"""
    tech_score: float = Field(default=0.0, ge=0.0, le=10.0, description="技术先进性评分 (1-10)")
    utility_score: float = Field(default=0.0, ge=0.0, le=10.0, description="实用性评分 (1-10)")
    community_score: float = Field(default=0.0, ge=0.0, le=10.0, description="社区活跃度评分 (1-10)")
    total_score: float = Field(default=0.0, ge=0.0, le=12.0, description="总评分 (含加分)")
    bonus: float = Field(default=0.0, ge=0.0, le=2.0, description="特别加分 (0-2)")
    status: AnalysisStatus = Field(default=AnalysisStatus.FAILED, description="状态")
    tags: List[str] = Field(default_factory=list, description="自动生成标签")
    summary: str = Field(default="", description="综合摘要")
    tech_summary: str = Field(default="", description="技术先进性摘要")
    utility_summary: str = Field(default="", description="实用性摘要")
    community_summary: str = Field(default="", description="社区活跃度摘要")


class LLMRawResult(BaseModel):
    """LLM 返回的原始评分结构（用于解析 API 响应）"""
    tech_score: float = Field(ge=1.0, le=10.0)
    utility_score: float = Field(ge=1.0, le=10.0)
    community_score: float = Field(ge=1.0, le=10.0)
    tech_summary: str = ""
    utility_summary: str = ""
    community_summary: str = ""
    summary: str = ""
    tags: List[str] = Field(default_factory=list)
    breakthrough: bool = Field(default=False, description="是否存在突破性创新")


class ReviewRecord(BaseModel):
    """人工复核记录"""
    project_id: str
    original_tech_score: float
    original_utility_score: float
    original_community_score: float
    reviewed_tech_score: float
    reviewed_utility_score: float
    reviewed_community_score: float
