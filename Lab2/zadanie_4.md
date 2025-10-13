Przygotować korutynę, która zwróci prognozę pogody dla najbliszej godziny dla miasta Zakopane. Wykorzystać w tym celu API Open-Meteo oraz przykładowy adres żądania: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m.

```python
import aiohttp
import asyncio
import datetime


async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            tabela = await response.json()
            return tabela


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.2992&longitude=19.9496&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    tab = await fetch(url)

    time_now = str(datetime.datetime.now().replace(minute=0,second=0,microsecond=0).isoformat(timespec='minutes'))
    index = tab['hourly']['time'].index(time_now)
    print(f"Aktualna pogoda w Zakopanem: {tab['hourly']['temperature_2m'][index]} stopni Celcjusza")
if __name__ == "__main__":
    asyncio.run(main())
```
