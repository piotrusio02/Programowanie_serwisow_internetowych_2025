from typing import Iterable

from domains.post import PostRecord
from repositories.post_repository import IPostRepository
from services.ipost_service import IPostService

class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        return await self.repository.get_all_posts()

    async def filter_posts(self, keywords: str) -> Iterable[PostRecord] | None:
        return await self.repository.filter_posts(keywords)

    async def get_posts_json(self) -> str:
        return await self.repository.get_posts_json()
