import asyncio
from concurrency.util.delay import delay


async def add_one(num: int) -> int:
    return num + 1


async def hello() -> str:
    await delay(1)
    return "Hello world!"


async def main() -> None:
    mes = await hello()
    res = await add_one(1)

    print(mes)
    print(res)


asyncio.run(main())
