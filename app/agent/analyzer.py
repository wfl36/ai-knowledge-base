"""项目分析器 - 调用 OpenRouter API 进行三维评分"""

import json
import os
from typing import Any, Dict, Optional

import httpx

from .models import AnalysisResult, AnalysisStatus, LLMRawResult

# ---------------------------------------------------------------------------
# 环境变量配置
# ---------------------------------------------------------------------------
DEFAULT_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "z-ai/glm-5.1"

SYSTEM_PROMPT = """\
你是一个专业的 AI 项目分析专家，负责对 AI 项目进行三维评分分析。

你需要从以下三个维度对项目进行评分（1-10 分），并给出详细的分析说明：

1. 技术先进性 (tech_score)：评估项目的技术创新程度、算法先进性、架构设计等
2. 实用性 (utility_score)：评估项目的实际应用价值、解决问题能力、易用性等
3. 社区活跃度 (community_score)：评估项目的社区参与度、维护活跃度、生态丰富度等

此外你需要：
- 判断项目是否存在突破性创新 (breakthrough)
- 为项目生成标签：技术类(如 深度学习/NLP/CV/强化学习/多模态 等)、
  应用类(如 聊天机器人/图像生成/代码助手/数据分析 等)、
  质量类(如 高质量/活跃维护/快速迭代/文档完善 等)
- 生成综合摘要

你必须严格按以下 JSON 格式返回结果，不要包含任何其他文本：
{
  "tech_score": <float 1-10>,
  "utility_score": <float 1-10>,
  "community_score": <float 1-10>,
  "tech_summary": "<技术先进性分析>",
  "utility_summary": "<实用性分析>",
  "community_summary": "<社区活跃度分析>",
  "summary": "<综合摘要>",
  "tags": ["<tag1>", "<tag2>", ...],
  "breakthrough": <bool>
}
"""


class ProjectAnalyzer:
    """通过 LLM API 对项目进行三维评分分析"""

    def __init__(
        self,
        api_url: Optional[str] = None,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ) -> None:
        self.api_url = api_url or os.getenv("LLM_API_URL", DEFAULT_API_URL)
        self.api_key = api_key or os.getenv("LLM_API_KEY", "")
        self.model = model or os.getenv("LLM_MODEL", DEFAULT_MODEL)

    # ------------------------------------------------------------------
    # 公开接口
    # ------------------------------------------------------------------
    async def analyze(self, project_info: str) -> AnalysisResult:
        """分析项目并返回三维评分结果。

        Args:
            project_info: 项目信息文本（README、描述等）

        Returns:
            AnalysisResult 完整分析结果
        """
        if not self.api_key:
            return AnalysisResult(status=AnalysisStatus.FAILED, summary="未配置 LLM_API_KEY")

        user_prompt = self._build_user_prompt(project_info)
        raw_result = await self._call_llm(user_prompt)
        if raw_result is None:
            return AnalysisResult(status=AnalysisStatus.FAILED, summary="LLM 调用失败或响应解析失败")

        return AnalysisResult(
            tech_score=raw_result.tech_score,
            utility_score=raw_result.utility_score,
            community_score=raw_result.community_score,
            total_score=0.0,  # 由 Scorer 计算
            bonus=0.0,        # 由 Scorer 计算
            status=AnalysisStatus.NORMAL,  # 由 Scorer 判定
            tags=raw_result.tags,
            summary=raw_result.summary,
            tech_summary=raw_result.tech_summary,
            utility_summary=raw_result.utility_summary,
            community_summary=raw_result.community_summary,
        )

    # ------------------------------------------------------------------
    # 内部方法
    # ------------------------------------------------------------------
    def _build_user_prompt(self, project_info: str) -> str:
        return (
            f"请对以下 AI 项目进行三维评分分析：\n\n"
            f"---\n{project_info}\n---\n\n"
            f"请严格按照 JSON 格式返回评分结果。"
        )

    async def _call_llm(self, user_prompt: str) -> Optional[LLMRawResult]:
        """调用 OpenRouter API 并解析响应"""
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.3,
            "response_format": {"type": "json_object"},
        }

        try:
            async with httpx.AsyncClient(timeout=120.0, http2=False) as client:
                resp = await client.post(self.api_url, json=payload, headers=headers)
                resp.raise_for_status()
                data = resp.json()

            content = data["choices"][0]["message"]["content"]
            parsed = json.loads(content)
            return LLMRawResult(**parsed)
        except (httpx.HTTPError, KeyError, json.JSONDecodeError, Exception) as exc:
            # 记录异常但不抛出，返回 None 让上层处理
            import logging
            logging.getLogger(__name__).error("LLM API 调用失败: %s", exc)
            return None
