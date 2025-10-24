import asyncio
from util.delay import delay

def call_later():
    print(f'Im being calling in the future!')

async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main(), debug=True)