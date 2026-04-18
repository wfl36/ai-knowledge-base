"""复核管理器 - 加载待复核项目、提交复核、历史管理"""

import json
import logging
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .models import (
    CompressedHistory,
    PendingProject,
    ReviewRecord,
    ReviewStatus,
    ScoreSet,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
PENDING_REVIEW_THRESHOLD = 6.0      # 总评分低于此值触发复核
ANOMALY_LOW = 3.0                   # 异常低阈值
ANOMALY_HIGH = 8.0                  # 异常高阈值

DEFAULT_HISTORY_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "review_history.json"
)
COMPRESSED_SUFFIX = "_compressed.json"


class ReviewManager:
    """人工复核管理器

    职责：
    - 判断分析结果是否需要复核（should_review）
    - 加载待复核项目列表（load_pending）
    - 提交复核结果（submit_review）
    - 管理复核历史（保存 / 加载 / 压缩）
    """

    def __init__(self, history_path: Optional[str] = None) -> None:
        self._history_path = Path(history_path or DEFAULT_HISTORY_PATH)

    # ------------------------------------------------------------------
    # should_review: 判断是否需要复核
    # ------------------------------------------------------------------
    @staticmethod
    def should_review(analysis_result) -> bool:
        """判断分析结果是否需要触发人工复核。

        触发条件（满足任一）：
        1. 总评分 < 6
        2. 任一维度评分异常：
           - 技术先进性 < 3 但实用性 > 8（或其他维度交叉异常）
           - 技术先进性 < 3 但社区活跃度 > 8
           - 实用性 < 3 但技术先进性 > 8
           - 实用性 < 3 但社区活跃度 > 8
           - 社区活跃度 < 3 但技术先进性 > 8
           - 社区活跃度 < 3 但实用性 > 8

        Args:
            analysis_result: app.agent.models.AnalysisResult 实例
                需要有 total_score, tech_score, utility_score, community_score 属性

        Returns:
            True 表示需要复核
        """
        total = getattr(analysis_result, "total_score", 0.0)
        tech = getattr(analysis_result, "tech_score", 0.0)
        utility = getattr(analysis_result, "utility_score", 0.0)
        community = getattr(analysis_result, "community_score", 0.0)

        # 条件1: 总评分 < 6
        if total < PENDING_REVIEW_THRESHOLD:
            return True

        # 条件2: 维度交叉异常 — 一个维度极低(<3)，另一个极高(>8)
        scores = {"tech": tech, "utility": utility, "community": community}
        keys = list(scores.keys())
        for i, k1 in enumerate(keys):
            for k2 in keys[i + 1:]:
                v1, v2 = scores[k1], scores[k2]
                if (v1 < ANOMALY_LOW and v2 > ANOMALY_HIGH) or \
                   (v2 < ANOMALY_LOW and v1 > ANOMALY_HIGH):
                    return True

        return False

    # ------------------------------------------------------------------
    # load_pending: 加载待复核项目列表
    # ------------------------------------------------------------------
    @staticmethod
    def load_pending(knowledge_dir: str) -> List[PendingProject]:
        """扫描知识库目录，解析 Markdown 文件中 status=待复核的项目。

        Markdown 文件格式约定（与 writer.py 输出一致）：
            # 项目名称
            **评分：** 5.0
            **状态：** 待复核

        Args:
            knowledge_dir: 知识库目录路径

        Returns:
            待复核项目列表
        """
        result: List[PendingProject] = []
        knowledge_path = Path(knowledge_dir)

        if not knowledge_path.exists():
            logger.warning("知识库目录不存在: %s", knowledge_dir)
            return result

        for md_file in knowledge_path.glob("*.md"):
            # 跳过 index.md
            if md_file.name == "index.md":
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                pending = _parse_md_for_pending(content, str(md_file))
                if pending is not None:
                    result.append(pending)
            except Exception as exc:
                logger.warning("解析文件失败 %s: %s", md_file, exc)

        return result

    # ------------------------------------------------------------------
    # submit_review: 提交复核结果
    # ------------------------------------------------------------------
    def submit_review(
        self,
        project_name: str,
        reviewer: str,
        modified_scores: ScoreSet,
        reason: str,
        original_scores: Optional[ScoreSet] = None,
    ) -> ReviewRecord:
        """提交一次人工复核。

        Args:
            project_name: 项目名称
            reviewer: 复核人员
            modified_scores: 修改后的三维评分
            reason: 修改原因
            original_scores: 原始评分（如果未提供则从历史文件中查找）

        Returns:
            创建的 ReviewRecord
        """
        if original_scores is None:
            # 尝试从最近的历史记录中获取原始评分
            original_scores = self._find_original_scores(project_name)

        record = ReviewRecord(
            project_name=project_name,
            review_time=datetime.now(),
            reviewer=reviewer,
            original_scores=original_scores,
            modified_scores=modified_scores,
            reason=reason,
            status=ReviewStatus.PENDING,
        )

        # 保存到历史
        self.save_review_history(record)
        logger.info(
            "已提交复核: project=%s, reviewer=%s, reason=%s",
            project_name, reviewer, reason,
        )
        return record

    def approve_review(self, record: ReviewRecord) -> ReviewRecord:
        """将复核记录标记为已通过。

        Args:
            record: 待审批的复核记录

        Returns:
            更新状态后的 ReviewRecord
        """
        updated = record.model_copy(update={"status": ReviewStatus.APPROVED})
        self._update_record_in_history(updated)
        logger.info("复核已通过: project=%s", record.project_name)
        return updated

    def reject_review(self, record: ReviewRecord) -> ReviewRecord:
        """将复核记录标记为已驳回。

        Args:
            record: 待审批的复核记录

        Returns:
            更新状态后的 ReviewRecord
        """
        updated = record.model_copy(update={"status": ReviewStatus.REJECTED})
        self._update_record_in_history(updated)
        logger.info("复核已驳回: project=%s", record.project_name)
        return updated

    # ------------------------------------------------------------------
    # 历史管理
    # ------------------------------------------------------------------
    def save_review_history(
        self,
        review_record: ReviewRecord,
        history_path: Optional[str] = None,
    ) -> None:
        """将复核记录追加保存到 JSON 文件。

        Args:
            review_record: 复核记录
            history_path: 历史文件路径（默认使用实例路径）
        """
        path = Path(history_path) if history_path else self._history_path
        path.parent.mkdir(parents=True, exist_ok=True)

        records = self.load_review_history(str(path))

        # 转换为可序列化字典
        new_entry = review_record.model_dump(mode="json")
        records.append(new_entry)

        path.write_text(
            json.dumps(records, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )
        logger.debug("复核记录已保存至 %s", path)

    def load_review_history(
        self,
        history_path: Optional[str] = None,
    ) -> List[dict]:
        """加载复核历史记录。

        Args:
            history_path: 历史文件路径（默认使用实例路径）

        Returns:
            原始字典列表（方便不同消费者自行解析）
        """
        path = Path(history_path) if history_path else self._history_path

        if not path.exists():
            return []

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                logger.warning("历史文件格式错误，期望列表: %s", path)
                return []
            return data
        except (json.JSONDecodeError, Exception) as exc:
            logger.warning("加载复核历史失败 %s: %s", path, exc)
            return []

    def load_review_records(
        self,
        history_path: Optional[str] = None,
    ) -> List[ReviewRecord]:
        """加载并解析复核历史为 ReviewRecord 对象列表。

        Args:
            history_path: 历史文件路径

        Returns:
            ReviewRecord 对象列表
        """
        raw = self.load_review_history(history_path)
        records: List[ReviewRecord] = []
        for item in raw:
            try:
                records.append(ReviewRecord(**item))
            except Exception as exc:
                logger.warning("解析复核记录失败: %s", exc)
        return records

    def compress_old_history(
        self,
        history_path: Optional[str] = None,
        months: int = 12,
    ) -> int:
        """压缩超过 N 个月的历史记录。

        将超出保留期的记录按月聚合为 CompressedHistory，保存到压缩文件，
        并从主历史文件中移除。保留期内的记录保持不变。

        压缩策略：
        - 每月压缩: 超出保留期的记录按月聚合
        - 每季度备份: 压缩文件按季度目录归档
        - 保留 N 个月: 默认 12 个月

        Args:
            history_path: 历史文件路径（默认使用实例路径）
            months: 保留月数（默认 12）

        Returns:
            压缩的记录数量
        """
        path = Path(history_path) if history_path else self._history_path

        if not path.exists():
            return 0

        cutoff = datetime.now() - timedelta(days=months * 30)

        # 加载所有记录
        all_records = self.load_review_records(str(path))
        if not all_records:
            return 0

        # 分离：保留期内的 vs 超出的
        recent: List[ReviewRecord] = []
        old: List[ReviewRecord] = []
        for rec in all_records:
            # 兼容 review_time 可能是字符串的情况
            rt = rec.review_time
            if isinstance(rt, str):
                try:
                    rt = datetime.fromisoformat(rt)
                except (ValueError, TypeError):
                    recent.append(rec)
                    continue
            if rt >= cutoff:
                recent.append(rec)
            else:
                old.append(rec)

        if not old:
            logger.info("无需压缩，所有记录均在保留期内")
            return 0

        # 按月分组聚合
        monthly: Dict[str, List[ReviewRecord]] = {}
        for rec in old:
            rt = rec.review_time
            if isinstance(rt, str):
                try:
                    rt = datetime.fromisoformat(rt)
                except (ValueError, TypeError):
                    rt = datetime.now()
            month_key = rt.strftime("%Y-%m")
            monthly.setdefault(month_key, []).append(rec)

        # 生成压缩摘要
        compressed_list: List[CompressedHistory] = []
        for month_key, recs in sorted(monthly.items()):
            tech_diffs, util_diffs, comm_diffs = [], [], []
            approved = rejected = 0
            for r in recs:
                tech_diffs.append(abs(r.original_scores.tech - r.modified_scores.tech))
                util_diffs.append(abs(r.original_scores.utility - r.modified_scores.utility))
                comm_diffs.append(abs(r.original_scores.community - r.modified_scores.community))
                if r.status == ReviewStatus.APPROVED:
                    approved += 1
                elif r.status == ReviewStatus.REJECTED:
                    rejected += 1

            n = len(recs)
            compressed_list.append(CompressedHistory(
                month=month_key,
                record_count=n,
                avg_tech_diff=round(sum(tech_diffs) / n, 2) if n else 0.0,
                avg_utility_diff=round(sum(util_diffs) / n, 2) if n else 0.0,
                avg_community_diff=round(sum(comm_diffs) / n, 2) if n else 0.0,
                approved_count=approved,
                rejected_count=rejected,
                summary=f"{month_key}: 共{n}条记录, 通过{approved}, 驳回{rejected}",
            ))

        # 保存压缩文件 — 按季度目录归档
        base_dir = path.parent
        for comp in compressed_list:
            year, month = comp.month.split("-")
            quarter = f"Q{(int(month) - 1) // 3 + 1}"
            quarter_dir = base_dir / "archive" / year / quarter
            quarter_dir.mkdir(parents=True, exist_ok=True)
            comp_file = quarter_dir / f"{comp.month}{COMPRESSED_SUFFIX}"

            # 合并已有压缩数据
            existing: List[dict] = []
            if comp_file.exists():
                try:
                    existing = json.loads(comp_file.read_text(encoding="utf-8"))
                except Exception:
                    pass
            if not isinstance(existing, list):
                existing = []

            existing.append(comp.model_dump(mode="json"))
            comp_file.write_text(
                json.dumps(existing, ensure_ascii=False, indent=2, default=str),
                encoding="utf-8",
            )

        # 用保留期内的记录覆写主文件
        recent_data = [r.model_dump(mode="json") for r in recent]
        path.write_text(
            json.dumps(recent_data, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

        logger.info(
            "历史压缩完成: 压缩 %d 条, 保留 %d 条",
            len(old), len(recent),
        )
        return len(old)

    # ------------------------------------------------------------------
    # 内部辅助
    # ------------------------------------------------------------------
    def _find_original_scores(self, project_name: str) -> ScoreSet:
        """从历史记录中查找项目的原始评分，找不到则返回零值。"""
        records = self.load_review_records()
        # 倒序查找最近一条
        for rec in reversed(records):
            if rec.project_name == project_name:
                return rec.original_scores
        return ScoreSet(tech=0.0, utility=0.0, community=0.0)

    def _update_record_in_history(self, updated: ReviewRecord) -> None:
        """更新历史文件中指定记录的状态。"""
        raw = self.load_review_history()
        if not raw:
            return

        # 找到匹配记录并更新
        target_time = updated.review_time
        if isinstance(target_time, datetime):
            target_iso = target_time.isoformat()
        else:
            target_iso = str(target_time)

        for item in raw:
            rec_time = item.get("review_time", "")
            if (item.get("project_name") == updated.project_name
                    and rec_time == target_iso):
                item["status"] = updated.status.value
                break

        self._history_path.write_text(
            json.dumps(raw, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )


# ---------------------------------------------------------------------------
# Markdown 解析辅助函数
# ---------------------------------------------------------------------------

# 预编译正则，提升大量文件扫描时的性能
_RE_TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_RE_STATUS = re.compile(r"\*\*状态：\*\*\s*(.+)", re.MULTILINE)
_RE_SCORE = re.compile(r"\*\*评分：\*\*\s*([\d.]+)", re.MULTILINE)


def _parse_md_for_pending(content: str, file_path: str) -> Optional[PendingProject]:
    """解析 Markdown 内容，如果状态为"待复核"则返回 PendingProject。

    Args:
        content: Markdown 文件内容
        file_path: 文件路径（用于 PendingProject.file_path）

    Returns:
        PendingProject 或 None
    """
    status_match = _RE_STATUS.search(content)
    if status_match is None:
        return None

    status_text = status_match.group(1).strip()
    if status_text != "待复核":
        return None

    # 提取项目名称
    title_match = _RE_TITLE.search(content)
    project_name = title_match.group(1).strip() if title_match else Path(file_path).stem

    # 提取评分
    score = 0.0
    score_match = _RE_SCORE.search(content)
    if score_match:
        try:
            score = float(score_match.group(1))
        except ValueError:
            pass

    return PendingProject(
        project_name=project_name,
        file_path=file_path,
        score=score,
        status_text=status_text,
    )
