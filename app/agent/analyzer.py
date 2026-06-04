"""项目分析器 - 调用 OpenRouter API 进行三维评分"""

import json
import logging
import os
from typing import Any, Dict, Optional

import httpx

from .models import AnalysisResult, AnalysisStatus, LLMRawResult
from .prompts import GITHUB_SYSTEM_PROMPT, get_system_prompt

# ---------------------------------------------------------------------------
# 环境变量配置
# ---------------------------------------------------------------------------
DEFAULT_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "z-ai/glm-5.1"

# 向后兼容: 旧引用 analyzer.SYSTEM_PROMPT 仍可用(= github 提示词)
SYSTEM_PROMPT = GITHUB_SYSTEM_PROMPT


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
    async def analyze(
        self,
        project_info: str,
        client: Optional[httpx.AsyncClient] = None,
        source_type: str = "github",
    ) -> AnalysisResult:
        """分析资源并返回三维评分结果。

        Args:
            project_info: 资源信息文本（标题、摘要、指标等）
            client: 可选的共享 httpx 客户端，用于复用连接（并发场景）
            source_type: 来源类型，决定使用哪套系统提示词

        Returns:
            AnalysisResult 完整分析结果
        """
        if not self.api_key:
            return AnalysisResult(status=AnalysisStatus.FAILED, summary="未配置 LLM_API_KEY")

        user_prompt = self._build_user_prompt(project_info)
        raw_result = await self._call_llm(
            user_prompt, client=client, system_prompt=get_system_prompt(source_type)
        )
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

    async def _call_llm(
        self,
        user_prompt: str,
        client: Optional[httpx.AsyncClient] = None,
        system_prompt: str = SYSTEM_PROMPT,
    ) -> Optional[LLMRawResult]:
        """调用 OpenRouter API 并解析响应。

        若传入 client 则复用其连接池；否则临时创建一个。
        """
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.3,
            "response_format": {"type": "json_object"},
        }

        try:
            if client is not None:
                resp = await client.post(self.api_url, json=payload, headers=headers)
                resp.raise_for_status()
                data = resp.json()
            else:
                async with httpx.AsyncClient(timeout=120.0, http2=False) as tmp_client:
                    resp = await tmp_client.post(self.api_url, json=payload, headers=headers)
                    resp.raise_for_status()
                    data = resp.json()

            content = data["choices"][0]["message"]["content"]
            parsed = json.loads(content)
            return LLMRawResult(**parsed)
        except Exception as exc:
            # 记录异常但不抛出，返回 None 让上层处理
            logging.getLogger(__name__).error("LLM API 调用失败: %s", exc, exc_info=True)
            return None
