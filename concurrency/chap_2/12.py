import asyncio
from asyncio import CancelledError
from concurrency.util.delay import delay


async def main():
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=1)
        print(f"result {result}")
    except asyncio.exceptions.TimeoutError:
        print("Got timeout but proceed!")
        await delay_task


asyncio.run(main())
