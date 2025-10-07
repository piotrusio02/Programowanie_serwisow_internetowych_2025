Utworzyć aplikację, która będzie symulowała pobieranie danych z innych usług sieciowych. W tym celu należy utworzyć korutynę fetch(delay: int), która po odczekaniu delay sekund zwróci dowolną wartość (symulacja pobierania danych z sieci). Następnie należy kilkukrotnie wywołać współbieżnie korutynę fetch z różnymi wartościami parametru delay. Podpowiedź: do współbieżnego wywołania wielu korutyn można wykorzystać funkcję gather, która zostanie umieszczona w dedykowanej korutynie. Wówczas nie ma potrzeby stosowania manualnego podejścia zarządzania zadaniami oraz pętlą zdarzeń.

```python
import asyncio

async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)
    print("pobrano w: " + str(delay) + " sekund.")
    return delay

async def main() -> None:
    await asyncio.gather(fetch(8), fetch(5), fetch(12), fetch(10))

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
