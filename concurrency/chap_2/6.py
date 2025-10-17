import asyncio
from concurrency.util.delay import delay


async def main():
    del_1 = asyncio.create_task(delay(3))
    del_2 = asyncio.create_task(delay(3))
    del_3 = asyncio.create_task(delay(3))

    await del_1
    await del_2
    await del_3


asyncio.run(main())
