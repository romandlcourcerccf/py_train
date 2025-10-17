import asyncio

from concurrency.util.delay import delay
from concurrency.util.timer import async_timer

import requests


@async_timer()
async def call_blocking() -> int:
    return requests.get("http://www.example.com")


@async_timer()
async def main():
    t1 = asyncio.create_task(call_blocking())
    t2 = asyncio.create_task(call_blocking())
    t3 = asyncio.create_task(call_blocking())

    await t1
    await t2
    await t3


asyncio.run(main())
