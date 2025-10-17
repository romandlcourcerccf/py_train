import asyncio

from concurrency.util.delay import delay
from concurrency.util.timer import async_timer


async def pos_integers_async(util: int):
    for integer in range(1, util):
        await delay(integer)
        yield integer


@async_timer()
async def main():
    as_gen = pos_integers_async(4)
    print(type(as_gen))

    async for num in as_gen:
        print(f"got num {num}")


asyncio.run(main())
