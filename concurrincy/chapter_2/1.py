import asyncio

async def delay(num: int) -> int:
    print(f'Start delay for {num}')
    await asyncio.sleep(num)
    print(f'Delay for {num} done')
    return num+1

async def ticker():
    for _ in range(3):
        await asyncio.sleep(1)
        print(f'Do something else!')
        
async def main():
    task1 = asyncio.create_task(delay(3))
    task2 = asyncio.create_task(delay(3))

    await ticker()
    await task1
    await task2

asyncio.run(main())

