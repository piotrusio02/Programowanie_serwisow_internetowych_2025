Przygotować program, który tworzy potok zadań asynchronicznych: żądanie do dowolnego API pobiera dane, następnie przetwarza je i finalnie zapisuje wynik na w systemie plików (np. w pliku tekstowym).
```Python
import aiohttp
import asyncio
import datetime


async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return weather

async def process(weather: dict) -> str:
    time_now = str(datetime.datetime.now().replace(minute=0, second=0, microsecond=0).isoformat(timespec='minutes'))
    index = weather['hourly']['time'].index(time_now)
    text = f"{datetime.datetime.fromisoformat(time_now)} -- Pogoda w Zakopanem: {weather['hourly']['temperature_2m'][index]} stopni Celcjusza"
    return text

async def save(text: str) -> None:
    file = open('plik.txt', 'a')
    file.write(f"{text} \n")
    file.close()

async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.2992&longitude=19.9496&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    weather = await fetch(url)
    text = await process(weather)
    final = await save(text)

if __name__ == "__main__":
    asyncio.run(main())
```
