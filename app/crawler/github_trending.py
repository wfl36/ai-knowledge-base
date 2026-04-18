"""GitHub Trending AI项目爬虫模块

抓取 GitHub Trending 页面，过滤 AI 相关项目，返回结构化数据。
"""

from __future__ import annotations

import asyncio
import logging
import random
import re
from typing import Optional

import httpx
from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Pydantic Model
# ---------------------------------------------------------------------------

class ProjectRaw(BaseModel):
    """爬虫原始产出——单个项目"""

    name: str
    description: str
    language: Optional[str] = None
    stars: int = 0
    forks: int = 0
    stars_today: int = 0
    url: str


# ---------------------------------------------------------------------------
# AI 关键词
# ---------------------------------------------------------------------------

AI_KEYWORDS: list[str] = [
    "ai",
    "prompt",
    "skills",
    "harness",
    "agent",
    "llm",
    "gpt",
    "transformer",
    "diffusion",
    "model",
    "neural",
    "deep-learning",
    "nlp",
    "computer-vision",
    "reinforcement-learning",
    "rag",
    "fine-tuning",
    "inference",
    "embedding",
    "tokenizer",
    "attention",
]

# 编译为不区分大小写的正则，匹配 whole word（含连字符词）
_AI_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(kw) for kw in AI_KEYWORDS) + r")\b",
    re.IGNORECASE,
)


def _is_ai_related(text: str) -> bool:
    """判断文本是否包含 AI 关键词"""
    return bool(_AI_PATTERN.search(text))


# ---------------------------------------------------------------------------
# 反爬配置
# ---------------------------------------------------------------------------

_USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) "
    "Gecko/20100101 Firefox/125.0",
]

_DEFAULT_DELAY_MIN = 2.0
_DEFAULT_DELAY_MAX = 3.0
_BACKOFF_DELAY_MIN = 6.0
_BACKOFF_DELAY_MAX = 10.0

_MAX_RETRIES = 3
_CONSECUTIVE_FAIL_THRESHOLD = 5


# ---------------------------------------------------------------------------
# 辅助：数字解析
# ---------------------------------------------------------------------------

def _parse_int(text: str) -> int:
    """将 '1,234' / '12.3k' / '' 等字符串转为 int"""
    if not text:
        return 0
    text = text.strip().replace(",", "")
    multiplier = 1
    if text.lower().endswith("k"):
        text = text[:-1]
        multiplier = 1_000
    try:
        return int(float(text) * multiplier)
    except ValueError:
        return 0


# ---------------------------------------------------------------------------
# 页面解析
# ---------------------------------------------------------------------------

def _parse_article(article: Tag) -> Optional[ProjectRaw]:
    """从单个 <article class="Box-row"> 解析项目信息"""

    # --- 项目名 & URL ---
    h2_tag = article.select_one("h2 a")
    if not h2_tag:
        return None
    # href 形如 "/owner/repo"
    href = h2_tag.get("href", "")
    if not href or href.count("/") != 2:
        return None
    name = href.lstrip("/")
    url = f"https://github.com/{name}"

    # --- 描述 ---
    desc_tag = article.select_one("p")
    description = desc_tag.get_text(strip=True) if desc_tag else ""

    # --- 语言 ---
    lang_tag = article.select_one('[itemprop="programmingLanguage"]')
    language: Optional[str] = None
    if lang_tag:
        language = lang_tag.get_text(strip=True) or None

    # --- star / fork ---
    # 两个 <a> 链接：第一个是 star 计数，第二个是 fork 计数
    link_tags = article.select("div a.Link--muted")
    stars = 0
    forks = 0
    if len(link_tags) >= 2:
        stars = _parse_int(link_tags[0].get_text(strip=True))
        forks = _parse_int(link_tags[1].get_text(strip=True))
    elif len(link_tags) == 1:
        stars = _parse_int(link_tags[0].get_text(strip=True))

    # --- 今日 star 增量 ---
    stars_today = 0
    today_tag = article.select_one("span.d-inline-block.float-sm-right")
    if today_tag:
        stars_today = _parse_int(today_tag.get_text(strip=True))

    return ProjectRaw(
        name=name,
        description=description,
        language=language,
        stars=stars,
        forks=forks,
        stars_today=stars_today,
        url=url,
    )


def _parse_page(html: str) -> list[ProjectRaw]:
    """解析单个 trending 页面，返回项目列表"""
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.select("article.Box-row")
    results: list[ProjectRaw] = []
    for article in articles:
        project = _parse_article(article)  # type: ignore[arg-type]
        if project:
            results.append(project)
    return results


# ---------------------------------------------------------------------------
# 爬虫主类
# ---------------------------------------------------------------------------

class GitHubTrendingCrawler:
    """GitHub Trending AI 项目异步爬虫

    用法::

        crawler = GitHubTrendingCrawler()
        projects = await crawler.crawl()
        for p in projects:
            print(p.name, p.stars_today)
    """

    # 要抓取的 URL 列表
    URLS: list[str] = [
        "https://github.com/trending",
        "https://github.com/trending?since=weekly",
    ]

    def __init__(self, max_projects: int = 20) -> None:
        self._max_projects = max_projects
        self._consecutive_failures = 0
        self._backoff_mode = False

    # ----- 内部：带重试的 GET 请求 -----

    async def _fetch(
        self,
        client: httpx.AsyncClient,
        url: str,
    ) -> str:
        """带重试与反爬策略的 GET 请求"""
        last_exc: Exception | None = None

        for attempt in range(1, _MAX_RETRIES + 1):
            try:
                # 选择随机 User-Agent
                headers = {"User-Agent": random.choice(_USER_AGENTS)}
                resp = await client.get(url, headers=headers, follow_redirects=True)
                resp.raise_for_status()

                # 请求间隔（先于重置，确保退避模式下也用较长延迟）
                lo, hi = (
                    (_BACKOFF_DELAY_MIN, _BACKOFF_DELAY_MAX)
                    if self._backoff_mode
                    else (_DEFAULT_DELAY_MIN, _DEFAULT_DELAY_MAX)
                )
                await asyncio.sleep(random.uniform(lo, hi))

                # 成功 → 重置连续失败计数
                self._consecutive_failures = 0
                self._backoff_mode = False

                return resp.text

            except (httpx.HTTPStatusError, httpx.RequestError) as exc:
                last_exc = exc
                self._consecutive_failures += 1
                logger.warning(
                    "请求 %s 失败 (第 %d 次, 连续 %d 次): %s",
                    url,
                    attempt,
                    self._consecutive_failures,
                    exc,
                )

                # 连续失败达到阈值 → 切换到退避策略
                if self._consecutive_failures >= _CONSECUTIVE_FAIL_THRESHOLD:
                    self._backoff_mode = True
                    logger.warning(
                        "连续失败 %d 次，切换到退避策略（延迟 %.0f-%.0fs）",
                        self._consecutive_failures,
                        _BACKOFF_DELAY_MIN,
                        _BACKOFF_DELAY_MAX,
                    )

                # 重试前等待（指数退避 + 抖动）
                base_delay = (
                    _BACKOFF_DELAY_MIN if self._backoff_mode else _DEFAULT_DELAY_MIN
                )
                wait = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
                await asyncio.sleep(wait)

        raise RuntimeError(
            f"请求 {url} 失败，已重试 {_MAX_RETRIES} 次"
        ) from last_exc

    # ----- 内部：AI 过滤 -----

    @staticmethod
    def _filter_ai_projects(projects: list[ProjectRaw]) -> list[ProjectRaw]:
        """根据 AI 关键词过滤项目"""
        result: list[ProjectRaw] = []
        for proj in projects:
            # 在项目名、描述中搜索关键词
            combined = f"{proj.name} {proj.description}"
            if _is_ai_related(combined):
                result.append(proj)
        return result

    # ----- 公开 API -----

    async def crawl(self) -> list[ProjectRaw]:
        """抓取所有 trending 页面，返回去重后的 AI 相关项目（最多 max_projects 条）"""
        seen_names: set[str] = set()
        ai_projects: list[ProjectRaw] = []

        async with httpx.AsyncClient(timeout=30.0) as client:
            for url in self.URLS:
                try:
                    html = await self._fetch(client, url)
                    projects = _parse_page(html)
                    filtered = self._filter_ai_projects(projects)
                    for proj in filtered:
                        if proj.name not in seen_names:
                            seen_names.add(proj.name)
                            ai_projects.append(proj)
                except RuntimeError:
                    logger.error("跳过 %s，所有重试均已失败", url)

        # 每天只取前 max_projects 条 AI 相关项目（不补充不足的情况）
        return ai_projects[: self._max_projects]
