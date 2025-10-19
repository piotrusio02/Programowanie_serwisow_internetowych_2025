import aiohttp
from typing import Iterable
from utils import consts
from domains.post import PostRecord
from repositories.ipost_repository import IPostRepository
import json

class PostRepository(IPostRepository):

    async def get_all_posts(self) -> Iterable[PostRecord] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_POST_URL) as response:
                if response.status != 200:
                    return None
                json_posts = await response.json()
                return [PostRecord(**post) for post in json_posts]

    async def filter_posts(self, keywords: str) -> Iterable[PostRecord] | None:
        all_posts = await self.get_all_posts()
        if all_posts is None:
            return None
        filtered = []
        for post in all_posts:
            if keywords.lower() in post.title.lower() or keywords.lower() in post.body.lower():
                filtered.append(post)
        return filtered

    async def get_posts_json(self) -> str:
        all_posts = await self.get_all_posts()
        json_posts = []
        for post in all_posts:
            json_posts.append({
                "userId": post.userId,
                "id": post.id,
                "title": post.title,
                "body": post.body
            })

        return json.dumps(json_posts)
