Zadanie polega na symulowaniu kuchni, w której kilku kucharzy przygotowuje różne posiłki równocześnie. Każdy posiłek składa się z kilku etapów, np. krojenie warzyw, gotowanie makaronu, smażenie mięsa. Każdy etap trwa określony czas i jest realizowany asynchronicznie. Kucharze przygotowują trzy różne dania. Każde danie wymaga wykonania trzech kroków, które trwają różny czas (np. krojenie – 2 sekundy, gotowanie – 5 sekund, smażenie – 3 sekundy).

```python
import asyncio

async def krojenie_warzyw(warzywa: list[str]) -> None:
    for i in warzywa:
        await asyncio.sleep(2) #krojenie jednego warzywa trwa 2 sekundy
        print("Pokrojono: " + i)

async def gotowanie(produkt: str) -> None:
    await asyncio.sleep(5)
    print("Ugotowano: " + produkt)

async def smazenie(mieso: str) -> None:
    await asyncio.sleep(3)
    print("Usmażono: " + mieso)

async def stworz(warzywa: list[str], produkt: str, mieso: str):
    await krojenie_warzyw(warzywa)
    await gotowanie(produkt)
    await smazenie(mieso)

async def main() -> None:
    await asyncio.gather(
        stworz(['brokuly', 'ziemniaki'],'ziemniaki','kotlet'),
        stworz(['pomidory'],'makaron','wolowe'),
        stworz(['ogorek','pomidor'],'ryz','kurczak')
    )

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
