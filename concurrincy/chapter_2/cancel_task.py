import asyncio
from asyncio import CancelledError
from util.delay import delay

async def main():

    long_task = asyncio.create_task(delay(10))
    sec_elapsed = 0

    while not long_task.done():

        print('Task not finished.')
        await asyncio.sleep(1)
        sec_elapsed +=1
        if sec_elapsed == 5:
            long_task.cancel()
        
    try:
        await long_task
    except CancelledError:
        print('Cancelled!')

asyncio.run(main())