from dependency_injector.wiring import Provide
import asyncio
from container import Container
from services.ipost_service import IPostService
import json

async def main(
        service: IPostService = Provide[Container.service],
) -> None:

    all_posts = await service.get_all_posts()

    keyword = "aspernatur a porro possimus"
    filtered_posts = await service.filter_posts(keyword)

    json_posts = await service.get_posts_json()

    print("Liczba wszystkich postów:", len(all_posts))
    print(f"Libcza postów zawierająca {keyword}: {len(filtered_posts)}")

    for i in filtered_posts:
        print(f"{i.id}. {i.title}")

    with open("post.json", "w") as file:
        json.dump(json.loads(json_posts), file, indent=1)
    print("Zapisano do post.json")

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())