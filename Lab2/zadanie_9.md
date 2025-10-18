Przygotować program, który wyśle asynchronicznie 100 żądań do dowolnego REST API i zachowa tylko te odpowiedzi, które mają kod statusu odpowiedzi w zakresie 200-299. W przypadku błędu serwera (kody 500-599), powinien ponowić próbę wysłania żądania maksymalnie 3 razy.

```Python
import aiohttp
import asyncio


async def fetch(session, url) -> int | None:
    for i in range(3):
        async with session.get(url) as response:
            status = response.status

            if 200 <= status < 300:
                return status
            elif 500 <= status < 600:
                continue
            else:
                return None
    return None

async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=10.95796&longitude=-63.84906&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for i in range(100)]

        all_status = await asyncio.gather(*tasks)
        print(all_status)
        results = []

        for i in all_status:
            if i is not None:
                results.append(i)
        print(results)

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
