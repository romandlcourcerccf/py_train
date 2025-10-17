import asyncio


async def delay(delay_secs: int) -> int:
    print("Go to sleep for {delay_secs}")
    await asyncio.sleep(delay_secs)
    print("Wake up after : {delay_secs}")
    return delay_secs
