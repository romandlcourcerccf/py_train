import asyncio
from asyncio import Future


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result(100)


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def main():
    future = make_request()
    val = await future
    print(val)


asyncio.run(main())
