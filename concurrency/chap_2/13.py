import asyncio
from concurrency.util.timer import async_timer


@async_timer()
async def delay(seconds: int):
    print(f"Start to sleep {seconds}")
    await asyncio.sleep(seconds)
    print(f"End to sleep {seconds}")
    return seconds


@async_timer()
async def main():
    t1 = asyncio.create_task(delay(2))
    t2 = asyncio.create_task(delay(2))

    await t1
    await t2


asyncio.run(main())
