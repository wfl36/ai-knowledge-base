"""GitHub Trending 信息源(薄封装现有爬虫)。

复用 app/crawler/github_trending.py 的爬虫逻辑，将 ProjectRaw 映射为通用 Item。
"""

from __future__ import annotations

import os
from typing import List

from app.crawler.github_trending import GitHubTrendingCrawler

from .base import BaseSource
from .models import Item


class GitHubTrendingSource(BaseSource):
    """GitHub Trending AI 项目源"""

    source_type = "github"

    def __init__(self, max_projects: int = 20) -> None:
        self._crawler = GitHubTrendingCrawler(max_projects=max_projects)

    @classmethod
    def from_env(cls) -> "GitHubTrendingSource":
        max_projects = int(os.getenv("GITHUB_MAX_PROJECTS", "20"))
        return cls(max_projects=max_projects)

    async def fetch(self) -> List[Item]:
        raw_projects = await self._crawler.crawl()
        return [
            Item(
                source_type=self.source_type,
                title=raw.name,
                url=raw.url,
                summary=raw.description,
                language=raw.language,
                metrics={
                    "stars": raw.stars,
                    "forks": raw.forks,
                    "stars_today": raw.stars_today,
                },
            )
            for raw in raw_projects
        ]
