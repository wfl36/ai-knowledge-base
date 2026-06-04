"""Hacker News 信息源(Algolia Search API)。

免鉴权:https://hn.algolia.com/api/v1/search?tags=story&query=...&numericFilters=points>=N
url 缺失(Ask HN 等自帖)时回退到 HN 讨论页,保证每条都有 https URL。
"""

from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import List

import httpx

from .base import BaseSource
from .models import Item

logger = logging.getLogger(__name__)

_API = "https://hn.algolia.com/api/v1/search"


class HackerNewsSource(BaseSource):
    """Hacker News AI 话题源"""

    source_type = "hackernews"

    def __init__(self, query: str, min_points: int = 50, max_items: int = 20) -> None:
        self._query = query
        self._min_points = min_points
        self._max_items = max_items

    @classmethod
    def from_env(cls) -> "HackerNewsSource":
        return cls(
            query=os.getenv("HN_QUERY", "AI OR LLM OR agent"),
            min_points=int(os.getenv("HN_MIN_POINTS", "50")),
            max_items=int(os.getenv("HN_MAX_ITEMS", "20")),
        )

    async def fetch(self) -> List[Item]:
        params = {
            "query": self._query,
            "tags": "story",
            "numericFilters": f"points>={self._min_points}",
            "hitsPerPage": self._max_items,
        }
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.get(_API, params=params)
                resp.raise_for_status()
                hits = resp.json().get("hits", [])
        except Exception as exc:
            logger.error("Hacker News 抓取失败: %s", exc)
            return []

        items: List[Item] = []
        seen: set = set()
        for hit in hits:
            object_id = hit.get("objectID", "")
            # url 缺失则回退到 HN 讨论页,保证链接区始终有 https URL
            url = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
            title = hit.get("title") or ""
            if not title:
                continue
            key = url.rstrip("/").lower()
            if key in seen:
                continue
            seen.add(key)

            published_at = None
            created = hit.get("created_at")
            if created:
                try:
                    published_at = datetime.fromisoformat(created.replace("Z", "+00:00"))
                except ValueError:
                    published_at = None

            items.append(
                Item(
                    source_type=self.source_type,
                    title=title.strip(),
                    url=url,
                    summary=hit.get("story_text") or "",
                    author=hit.get("author"),
                    published_at=published_at,
                    metrics={
                        "points": hit.get("points", 0),
                        "num_comments": hit.get("num_comments", 0),
                    },
                )
            )
        return items
