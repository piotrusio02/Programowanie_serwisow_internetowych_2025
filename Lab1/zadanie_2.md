Utwórz korutynę, która wyświetla wiadomość "Hello" po jednej sekundzie i "world" po dwóch sekundach.

```python
import asyncio

async def main() -> None:
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(2)
    print("World")

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
```
