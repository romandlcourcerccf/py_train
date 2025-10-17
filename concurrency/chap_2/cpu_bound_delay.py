import asyncio

from concurrency.util.delay import delay
from concurrency.util.timer import async_timer


@async_timer()
async def cpu_bound() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


@async_timer()
async def main():
    t1 = asyncio.create_task(cpu_bound())
    t2 = asyncio.create_task(cpu_bound())

    delay_task = asyncio.create_task(delay(4))

    await t1
    await t2
    await delay_task


asyncio.run(main())
