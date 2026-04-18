"""评分计算与动态权重调整"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional

from .models import (
    AnalysisResult,
    AnalysisStatus,
    ReviewRecord,
    WeightConfig,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
DEFAULT_WEIGHTS_DIR = os.path.dirname(os.path.abspath(__file__))
WEIGHTS_FILENAME = "weights.json"
REVIEW_HISTORY_FILENAME = "review_history.json"

# 动态权重调整参数
MIN_WEIGHT = 0.20   # 单维度最低权重
MAX_WEIGHT = 0.50   # 单维度最高权重
MAX_ADJUSTMENT = 0.05  # 单次最大调整幅度 ±5%

# 特别加分阈值
BONUS_THRESHOLD = 9.0  # 任一维度 >= 9 触发加分评估
MAX_BONUS = 2.0

# 待复核阈值
PENDING_REVIEW_THRESHOLD = 6.0


class WeightManager:
    """管理评分权重，支持动态调整。

    权重调整策略（参考淘宝店铺评分算法）：
    - 某维度自动评分与人工复核越一致 → 该维度权重增加
    - 差异越大 → 该维度权重降低
    - 单次调整不超过 ±5%
    - 权重范围 20%~50%
    - 调整后重新归一化
    """

    def __init__(self, weights_dir: Optional[str] = None) -> None:
        self._weights_dir = Path(weights_dir or DEFAULT_WEIGHTS_DIR)
        self._weights_path = self._weights_dir / WEIGHTS_FILENAME
        self._review_path = self._weights_dir / REVIEW_HISTORY_FILENAME
        self._config = self._load_weights()

    # ------------------------------------------------------------------
    # 属性
    # ------------------------------------------------------------------
    @property
    def config(self) -> WeightConfig:
        return self._config

    # ------------------------------------------------------------------
    # 权重读写
    # ------------------------------------------------------------------
    def _load_weights(self) -> WeightConfig:
        if self._weights_path.exists():
            try:
                data = json.loads(self._weights_path.read_text(encoding="utf-8"))
                return WeightConfig(**data)
            except (json.JSONDecodeError, Exception) as exc:
                logger.warning("权重文件读取失败，使用默认值: %s", exc)
        return WeightConfig()  # 默认各 1/3

    def save_weights(self) -> None:
        self._weights_path.write_text(
            self._config.model_dump_json(indent=2),
            encoding="utf-8",
        )
        logger.info("权重已保存至 %s", self._weights_path)

    # ------------------------------------------------------------------
    # 动态调整
    # ------------------------------------------------------------------
    def adjust_from_reviews(self) -> bool:
        """根据历史复核记录动态调整权重。

        读取 review_history.json 中的复核记录，对比自动评分与人工评分的
        差异，按维度调整权重并持久化。

        Returns:
            True 如果权重发生了变化
        """
        records = self._load_review_history()
        if not records:
            logger.info("无复核记录，权重不变")
            return False

        # 累计各维度偏差
        tech_diff_sum = 0.0
        util_diff_sum = 0.0
        comm_diff_sum = 0.0
        count = 0

        for rec in records:
            tech_diff_sum += abs(rec.original_tech_score - rec.reviewed_tech_score)
            util_diff_sum += abs(rec.original_utility_score - rec.reviewed_utility_score)
            comm_diff_sum += abs(rec.original_community_score - rec.reviewed_community_score)
            count += 1

        if count == 0:
            return False

        avg_tech_diff = tech_diff_sum / count
        avg_util_diff = util_diff_sum / count
        avg_comm_diff = comm_diff_sum / count

        # 差异越小 → 增加权重；差异越大 → 降低权重
        # 用一个简单的线性映射：diff=0 → +5%, diff=5 → -5%
        tech_adj = self._diff_to_adjustment(avg_tech_diff)
        util_adj = self._diff_to_adjustment(avg_util_diff)
        comm_adj = self._diff_to_adjustment(avg_comm_diff)

        new_weights = self._apply_adjustments(
            tech_adj=tech_adj,
            util_adj=util_adj,
            comm_adj=comm_adj,
        )

        changed = (
            new_weights.tech_weight != self._config.tech_weight
            or new_weights.utility_weight != self._config.utility_weight
            or new_weights.community_weight != self._config.community_weight
        )

        if changed:
            self._config = new_weights
            self.save_weights()
            logger.info("权重已动态调整: tech=%.4f util=%.4f comm=%.4f",
                        self._config.tech_weight,
                        self._config.utility_weight,
                        self._config.community_weight)

        return changed

    # ------------------------------------------------------------------
    # 内部方法
    # ------------------------------------------------------------------
    @staticmethod
    def _diff_to_adjustment(avg_diff: float) -> float:
        """将平均偏差映射为调整量。

        diff=0 → +0.05  (完全一致，增加权重)
        diff=2.5 → 0    (适中，不调整)
        diff=5+ → -0.05 (差异很大，降低权重)
        """
        adj = 0.05 - (avg_diff / 2.5) * 0.05
        adj = max(-MAX_ADJUSTMENT, min(MAX_ADJUSTMENT, adj))
        return round(adj, 4)

    def _apply_adjustments(
        self,
        tech_adj: float,
        util_adj: float,
        comm_adj: float,
    ) -> WeightConfig:
        """应用调整量并归一化"""
        new_tech = self._config.tech_weight + tech_adj
        new_util = self._config.utility_weight + util_adj
        new_comm = self._config.community_weight + comm_adj

        # 钳制到 [MIN_WEIGHT, MAX_WEIGHT]
        new_tech = max(MIN_WEIGHT, min(MAX_WEIGHT, new_tech))
        new_util = max(MIN_WEIGHT, min(MAX_WEIGHT, new_util))
        new_comm = max(MIN_WEIGHT, min(MAX_WEIGHT, new_comm))

        # 归一化
        total = new_tech + new_util + new_comm
        new_tech /= total
        new_util /= total
        new_comm /= total

        return WeightConfig(
            tech_weight=round(new_tech, 4),
            utility_weight=round(new_util, 4),
            community_weight=round(new_comm, 4),
        )

    def _load_review_history(self) -> List[ReviewRecord]:
        if not self._review_path.exists():
            return []
        try:
            data = json.loads(self._review_path.read_text(encoding="utf-8"))
            return [ReviewRecord(**r) for r in data]
        except (json.JSONDecodeError, Exception) as exc:
            logger.warning("复核历史读取失败: %s", exc)
            return []


class Scorer:
    """评分计算器：加权评分 + 特别加分 + 状态判定"""

    def __init__(self, weight_manager: Optional[WeightManager] = None) -> None:
        self._wm = weight_manager or WeightManager()

    # ------------------------------------------------------------------
    # 公开接口
    # ------------------------------------------------------------------
    def score(self, result: AnalysisResult, human_confirm_bonus: bool = False) -> AnalysisResult:
        """对 AnalysisResult 进行加权评分、加分判定和状态标记。

        Args:
            result: 包含三维原始评分的分析结果（通常来自 ProjectAnalyzer）
            human_confirm_bonus: 人工是否确认特别加分

        Returns:
            更新了 total_score / bonus / status 的 AnalysisResult
        """
        wc = self._wm.config

        # 加权评分
        weighted = (
            result.tech_score * wc.tech_weight
            + result.utility_score * wc.utility_weight
            + result.community_score * wc.community_weight
        )

        # 特别加分
        bonus = self._calc_bonus(result, human_confirm_bonus)

        total_score = round(weighted + bonus, 2)

        # 状态判定
        if result.status == AnalysisStatus.FAILED:
            status = AnalysisStatus.FAILED
        elif total_score < PENDING_REVIEW_THRESHOLD:
            status = AnalysisStatus.PENDING_REVIEW
        else:
            status = AnalysisStatus.NORMAL

        # 返回更新后的结果（创建新对象避免原地修改）
        return result.model_copy(
            update={
                "total_score": total_score,
                "bonus": bonus,
                "status": status,
            }
        )

    def adjust_weights(self) -> bool:
        """触发权重动态调整（代理 WeightManager）"""
        return self._wm.adjust_from_reviews()

    @property
    def weight_config(self) -> WeightConfig:
        return self._wm.config

    # ------------------------------------------------------------------
    # 内部方法
    # ------------------------------------------------------------------
    @staticmethod
    def _calc_bonus(result: AnalysisResult, human_confirm: bool) -> float:
        """计算特别加分。

        触发条件（满足任一即可申请加分）：
        1. 任一维度评分 >= BONUS_THRESHOLD (9)
        2. LLM 标记了 breakthrough

        加分规则：
        - 基础加分 = max(各超出部分) 的线性映射，上限 MAX_BONUS
        - 必须人工确认才生效
        """
        triggered = False
        base_bonus = 0.0

        # 检查维度是否 >= 9
        scores = [result.tech_score, result.utility_score, result.community_score]
        max_score = max(scores)
        if max_score >= BONUS_THRESHOLD:
            triggered = True
            # 超出 9 的部分映射到 [0, MAX_BONUS]
            # score=9 → 0, score=10 → MAX_BONUS
            base_bonus = max(0.0, (max_score - BONUS_THRESHOLD) / (10.0 - BONUS_THRESHOLD) * MAX_BONUS)

        # 检查是否有 breakthrough 标记（通过 tags 或额外字段）
        # 由于 AnalysisResult 本身没有 breakthrough 字段，我们通过 tags 判断
        # 如果需要可以扩展；这里给一个固定 1 分基础加分
        if "突破性创新" in (result.tags or []):
            triggered = True
            base_bonus = max(base_bonus, 1.0)

        if not triggered:
            return 0.0

        if not human_confirm:
            return 0.0  # 未确认不加分

        return round(min(base_bonus, MAX_BONUS), 2)
