from abc import ABC
from typing import Iterable
from domains.post import PostRecord

class IPostService(ABC):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        pass

    async def filter_posts(self, keywords: str) -> Iterable[PostRecord] | None:
        pass

    async def get_posts_json(self) -> str:
        pass