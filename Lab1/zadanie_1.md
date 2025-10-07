Utworzyć korutynę, która wstrzymuje działanie na 2 sekundy, a potem wyświetla komunikat o treści "Oczekiwanie zakończone".

```python
import asyncio

async def main() -> None:
    await asyncio.sleep(1)
    print("Oczekiwanie zakończone")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
