Przygotować korutynę, która asynchronicznie pobiera i zwraca zawartość strony internetowej z podanego adresu URL przy użyciu biblioteki aiohttp.

```python
import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main() -> None:
    url = "https://krzywicki.pro/teaching/"
    zawartosc = await fetch(url)
    print(zawartosc)

if __name__ == "__main__":
    asyncio.run(main())
```
