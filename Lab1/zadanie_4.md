Utworzyć aplikację, która co sekundę wyświetla kolejne liczby od 1 do 5. Należy pamiętać o zastosowaniu podejścia asynchronicznego!

```python
import asyncio

async def main() -> None:
    for i in range(1,6):
        await asyncio.sleep(1)
        print(i)

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
