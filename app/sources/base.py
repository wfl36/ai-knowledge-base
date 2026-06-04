"""信息源插件基类

新增一个信息源 = 新增一个 BaseSource 子类文件，并在
app/sources/__init__.py 的注册表里登记。
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from .models import Item


class BaseSource(ABC):
    """信息源抽象基类。

    约定: 每个源自行管理其 HTTP 客户端与异常处理，
    fetch() 失败应尽量返回空列表而非抛出，避免拖垮整条 pipeline。
    """

    #: 来源类型标识，子类必须覆盖(如 "github" / "rss" / "hackernews")
    source_type: str = "base"

    @abstractmethod
    async def fetch(self) -> List[Item]:
        """抓取并返回该来源的资源列表(已去重)。"""
        raise NotImplementedError
