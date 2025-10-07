Utworzyć dwie korutyny, a nstępnie je uruchomić współbienie. Obie korutyny będą miały takie samo działanie: oczekują zadaną ilość czasu, a następnie wyświetlają komunikat. Niech pierwsza z nich czeka trzy sekundy, a druga jedną sekundę.

```python
import asyncio

async def k1() -> None:
    await asyncio.sleep(3)
    print("korutyna 1")

async def k2() -> None:
    await asyncio.sleep(1)
    print("korutyna 2")

async def main() -> None:
    await asyncio.gather(k1(), k2())

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
