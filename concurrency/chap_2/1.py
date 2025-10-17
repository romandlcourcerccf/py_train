import asyncio
from concurrency.util.delay import delay


async def hello():
    await delay(1)
    return "Hello!"


async def main():
    mes = await hello()
    print(mes)


asyncio.run(main())
