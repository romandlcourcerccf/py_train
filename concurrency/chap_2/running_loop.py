import asyncio


async def delay():
    await asyncio.sleep(3)
    print("done")


def call():
    print("Im called later!")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call)
    await delay()


asyncio.run(main(), debug=True)
