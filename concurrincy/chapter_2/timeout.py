import asyncio
from util.delay import delay

async def main():

    delay_task = asyncio.create_task(delay(2))

    try:
        res = await asyncio.wait_for(delay_task, timeout=1)
        print(res)
    except asyncio.exceptions.TimeoutError:
        print('Got timeout!')
        print(f'Was the task cancelled {delay_task.cancelled()}')

asyncio.run(main())
