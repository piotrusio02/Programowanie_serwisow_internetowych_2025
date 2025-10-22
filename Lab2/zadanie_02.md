Przygotować korutynę, która asynchronicznie wyśle żądanie POST do REST API z treścią w formacie JSON i zwróci odpowiedź.

```python
import aiohttp
import asyncio

async def add_user(url: str, body: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=body) as response:
            return await response.json()


async def main() -> None:
    url = "https://68e68acb21dd31f22cc61897.mockapi.io/api/test/serwisy/users"
    body = {
    "imie": "Piotr",
    "nazwisko": "Piotrowski",
    "id": "62"
    }
    users = await add_user(url=url, body=body)

    print(users)

if __name__ == "__main__":
    asyncio.run(main())
```
