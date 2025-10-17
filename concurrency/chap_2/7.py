import asyncio
from concurrency.util.delay import delay


async def print_hello():
    for _ in range(2):
        await asyncio.sleep(1)
        print("Just running other code!")


async def main():
    del_1 = asyncio.create_task(delay(3))
    del_2 = asyncio.create_task(delay(3))
    await print_hello()

    await del_1
    await del_2


asyncio.run(main())
