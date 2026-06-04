"""RSS / Atom 信息源(arXiv 论文 + 厂商/工程博客)。

arXiv 的 RSS 即标准 RSS，无需特殊处理。feedparser.parse 为阻塞调用，
统一用 asyncio.to_thread 包裹，多个 feed 并发抓取。
"""

from __future__ import annotations

import asyncio
import logging
import os
from datetime import datetime
from typing import List, Optional

import feedparser
from bs4 import BeautifulSoup

from .base import BaseSource
from .models import Item

logger = logging.getLogger(__name__)

# 默认订阅源:arXiv cs.AI / cs.CL + HuggingFace 博客(均提供标准 RSS/Atom)
DEFAULT_FEEDS = [
    "http://export.arxiv.org/rss/cs.AI",
    "http://export.arxiv.org/rss/cs.CL",
    "https://huggingface.co/blog/feed.xml",
]


def _clean_html(text: str) -> str:
    """去除摘要中的 HTML 标签，压缩空白。"""
    if not text:
        return ""
    txt = BeautifulSoup(text, "html.parser").get_text(separator=" ")
    return " ".join(txt.split())


def _parse_published(entry) -> Optional[datetime]:
    pp = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if pp:
        try:
            return datetime(*pp[:6])
        except (TypeError, ValueError):
            return None
    return None


class RSSSource(BaseSource):
    """RSS/Atom 文章源"""

    source_type = "rss"

    def __init__(self, feeds: List[str], max_per_feed: int = 10) -> None:
        self._feeds = feeds
        self._max_per_feed = max_per_feed

    @classmethod
    def from_env(cls) -> "RSSSource":
        raw = os.getenv("RSS_FEEDS", "").strip()
        feeds = [f.strip() for f in raw.split(",") if f.strip()] if raw else list(DEFAULT_FEEDS)
        max_per_feed = int(os.getenv("RSS_MAX_PER_FEED", "10"))
        return cls(feeds=feeds, max_per_feed=max_per_feed)

    def _parse_feed(self, feed_url: str) -> List[Item]:
        """同步解析单个 feed(在线程中执行)。"""
        parsed = feedparser.parse(feed_url)
        items: List[Item] = []
        for entry in parsed.entries[: self._max_per_feed]:
            link = getattr(entry, "link", "") or ""
            title = getattr(entry, "title", "") or ""
            if not link or not title:
                continue
            items.append(
                Item(
                    source_type=self.source_type,
                    title=title.strip(),
                    url=link.strip(),
                    summary=_clean_html(getattr(entry, "summary", "")),
                    author=getattr(entry, "author", None),
                    published_at=_parse_published(entry),
                )
            )
        return items

    async def fetch(self) -> List[Item]:
        async def _one(feed_url: str) -> List[Item]:
            try:
                return await asyncio.to_thread(self._parse_feed, feed_url)
            except Exception as exc:
                logger.error("RSS feed 抓取失败 %s: %s", feed_url, exc)
                return []

        results = await asyncio.gather(*(_one(f) for f in self._feeds))

        # 源内按 url 去重
        seen: set = set()
        merged: List[Item] = []
        for batch in results:
            for it in batch:
                key = it.url.rstrip("/").lower()
                if key in seen:
                    continue
                seen.add(key)
                merged.append(it)
        return merged
