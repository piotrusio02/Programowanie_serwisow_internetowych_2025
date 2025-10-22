Przygotować program, który asynchronicznie pobierze plik binarny za pomocą wskazanego URL (np. obraz, wideo, nagranie) z sieci, a następnie zapisze go na dysku lokalnym pod wskazaną ścieżką.
```Python
import aiohttp
import asyncio

async def download(url: str, path: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()

            with open(path, "wb") as plik:
                plik.write(content)

async def main() -> None:
    url = "https://zooart.com.pl/blog/wp-content/uploads/2022/03/FOTO-WESTIE-SZCZENIAK-1000x667-1.jpg"
    path = "./westie.jpg"
    await download(url,path)

if __name__ == "__main__":
    asyncio.run(main())
```
