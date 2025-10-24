import asyncio

from util.timer import async_timed

@async_timed()
async def delay(delay_in_seconds: int) -> int:
    print(f'Sleep for {delay_in_seconds}')
    await asyncio.sleep(delay_in_seconds)
    print(f'Awake after {delay_in_seconds}')

@async_timed()
async def main():

    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())
