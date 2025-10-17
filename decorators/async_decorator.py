import functools
import time
import asyncio


def async_timer(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        s = time.perf_counter()
        await fn(*args, **kwargs)
        print(time.perf_counter() - s)

    return wrapper


@async_timer
async def my_func():
    asyncio.timeout(1)


asyncio.run(my_func())
