"""信息源插件包与注册表。

启用哪些源由环境变量 AKB_SOURCES 控制(逗号分隔)，例如:
    AKB_SOURCES=github,rss,hackernews

新增一个源 = 新增一个 BaseSource 子类文件 + 在 _FACTORIES 里登记一行。
"""

from __future__ import annotations

import logging
import os
from typing import Callable, List

from .base import BaseSource
from .models import Item

logger = logging.getLogger(__name__)

__all__ = ["Item", "BaseSource", "build_sources"]

DEFAULT_SOURCES = "github"


def _make_github() -> BaseSource:
    from .github_trending import GitHubTrendingSource
    return GitHubTrendingSource.from_env()


def _make_rss() -> BaseSource:
    from .rss import RSSSource
    return RSSSource.from_env()


def _make_hackernews() -> BaseSource:
    from .hackernews import HackerNewsSource
    return HackerNewsSource.from_env()


# token -> 工厂(惰性导入，未实现/导入失败的源会被跳过)
_FACTORIES: dict[str, Callable[[], BaseSource]] = {
    "github": _make_github,
    "rss": _make_rss,
    "hackernews": _make_hackernews,
}


def build_sources(spec: str | None = None) -> List[BaseSource]:
    """根据 AKB_SOURCES 构造启用的信息源列表。

    Args:
        spec: 逗号分隔的来源标识；为 None 时读取环境变量 AKB_SOURCES。

    Returns:
        已启用且可用的 BaseSource 实例列表(顺序去重)；未知或导入失败的源跳过。
    """
    raw = spec if spec is not None else os.getenv("AKB_SOURCES", DEFAULT_SOURCES)
    tokens = [t.strip().lower() for t in raw.split(",") if t.strip()]

    sources: List[BaseSource] = []
    seen: set[str] = set()
    for token in tokens:
        if token in seen:
            continue
        seen.add(token)
        factory = _FACTORIES.get(token)
        if factory is None:
            logger.warning("未知信息源 '%s'，已跳过(可选: %s)", token, ", ".join(_FACTORIES))
            continue
        try:
            sources.append(factory())
        except Exception as exc:  # 导入失败/配置缺失等，跳过该源而非中断
            logger.error("信息源 '%s' 初始化失败，已跳过: %s", token, exc)

    return sources
