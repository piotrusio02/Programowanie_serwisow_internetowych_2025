Zadanie polega na symulacji harmonogramu pracy w fabryce, gdzie różne maszyny wykonują swoje zadania w ustalonych przedziałach czasu. Maszyny muszą czekać na zakończenie poprzedniego cyklu zanim zaczną kolejny. Ustalić, aby każda maszyna działała w innym tempie, a wszystkie zadania były asynchroniczne. Każda maszyna ma swój cykl pracy, który powtarza się w określonym czasie (np. maszyna A – co 2 sekundy, maszyna B – co 3 sekundy, maszyna C – co 5 sekund). Należy zasymulować ich działanie przez 15 sekund.

```python
import asyncio
import time

async def maszyna_a(czas: int) -> None:
    start = time.time()
    while time.time() - start  < czas:
        print("poczatek pracy maszyny a")
        await asyncio.sleep(2)
        print("koniec pracy maszyny a")

async def maszyna_b(czas: int) -> None:
    start = time.time()
    while time.time() - start  < czas:
        print("poczatek pracy maszyny b")
        await asyncio.sleep(3)
        print("koniec pracy maszyny b")

async def maszyna_c(czas: int) -> None:
    start = time.time()
    while time.time() - start  < czas:
        print("poczatek pracy maszyny c")
        await asyncio.sleep(5)
        print("koniec pracy maszyny c")

async def main() -> None:
    czas = 15
    await asyncio.gather(maszyna_a(czas), maszyna_b(czas), maszyna_c(czas))

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
