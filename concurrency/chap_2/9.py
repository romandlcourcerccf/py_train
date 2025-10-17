import asyncio
from concurrency.util.delay import delay
from asyncio import CancelledError


async def main():
    
    long_task = asyncio.create_task(delay(10))
    elapsed = 0

    while not long_task.done():
        print("Not finished yet")
        await asyncio.sleep(1)
        elapsed += 1
        if elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("Cancelled")


asyncio.run(main())
