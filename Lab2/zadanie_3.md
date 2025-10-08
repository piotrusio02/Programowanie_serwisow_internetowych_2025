Przygotować program, który asynchronicznie pobiera treści z 5 różnych (dowolnych) stron internetowych w sposób współbieżny.

```python
import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main() -> None:
    print(await asyncio.gather(fetch('https://krzywicki.pro/teaching/'),
                         fetch('http://wmii.uwm.edu.pl'),
                         fetch('https://uwm.edu.pl'),
                         fetch('https://piojas.pl'),
                         fetch('https://kortowiada.pl')))
    
if __name__ == "__main__":
    asyncio.run(main())
```
