Zadanie polega na symulowaniu przetwarzania pięciu dużych plików, gdzie każdy plik musi przejść przez kilka etapów przetwarzania, takich jak wczytanie, analiza i zapis. Każdy z tych kroków trwa określony czas i musi być wykonany asynchronicznie. Każdy plik przechodzi przez trzy etapy: wczytanie (2 sekundy), analiza (4 sekundy), zapis (1 sekunda). Symuluj asynchroniczne przetwarzanie wszystkich plików naraz.

```python
import asyncio

async def przetwarzanie(plik: str) -> None:
    print("Wczytywanie pliku: " + plik)
    await asyncio.sleep(2)
    print("Analiza pliku: " + plik)
    await asyncio.sleep(4)
    print("Zapisywanie pliku: " + plik)
    await asyncio.sleep(1)
    print("plik: " + plik + " Został zapisany")

async def main() -> None:
    await asyncio.gather(
        przetwarzanie('plik 1'),
        przetwarzanie('plik tekstowy 1'),
        przetwarzanie('plik 2'),
        przetwarzanie('plik 3'),
        przetwarzanie('plik tekstowy 2')
    )

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
