import asyncio

async def delay(num: int) -> int:
    print(f'Start delay for {num}')
    await asyncio.sleep(num)
    print(f'Delay for {num} done')
    return num+1
