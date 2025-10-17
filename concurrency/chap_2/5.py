import asyncio
from concurrency.util.delay import delay


async def main():
    sleep_task = asyncio.create_task(delay(3))
    print(type(sleep_task))
    res = await sleep_task
    print(res)


asyncio.run(main())
