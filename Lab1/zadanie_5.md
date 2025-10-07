Utworzyć aplikację, która będzie wykonywała się przez N sekund, co sekundę wyświetlając kolejną liczbę ciągu Fibonacciego.

```python
import asyncio

async def main(n: int) -> None:
    a = 0
    b = 1
    for i in range(n):
        await asyncio.sleep(1)
        print(a)
        a = b
        b = a + b

if __name__ == "__main__":
    n = int(input("Poddajj ilość sekund: "))
    with asyncio.Runner() as runner:
        runner.run(main(n))
```
