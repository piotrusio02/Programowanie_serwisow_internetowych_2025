Przygotować korutynę, która pobierze współbieżnie prognozę pogody dla miast Porlamar, Moroni i Helsinek, 
a następnie zwróci słownik zawierający klucze odpowiadające nazwom tych miast z wartościami prognozy pogody na najbliższą godzinę.

```Python
import aiohttp
import asyncio
import datetime


async def fetch(session, dictionary: dict) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={dictionary.get('latitude')}&longitude={dictionary.get('longitude')}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    async with session.get(url) as response:
        wynik = await response.json()
        return wynik

async def final(wynik: dict) -> dict:
    time_now = str(datetime.datetime.now().replace(minute=0, second=0, microsecond=0).isoformat(timespec='minutes'))
    pogoda = {}
    for i, j in wynik.items():
        index = j['hourly']['time'].index(time_now)
        temperatura = j['hourly']['temperature_2m'][index]
        pogoda[i] = temperatura
    return pogoda


async def main() -> None:
    miasta = {
        "Porlamar": {"latitude": 10.95796, "longitude": -63.84906},
        "Moroni": {"latitude": -11.749997, "longitude": 43.1999992},
        "Helsinki": {"latitude": 60.16952, "longitude": 24.93545}
    }

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, dictionary) for dictionary in miasta.values()]

        wyniki = await asyncio.gather(*tasks)
        slownik_miast = dict(zip(miasta.keys(), wyniki))
        pogoda = await final(slownik_miast)

        print(pogoda)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task = loop.create_task(main())
    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)
    for pending_task in pending:
        pending_task.cancel()

    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)

    loop.close()
```
