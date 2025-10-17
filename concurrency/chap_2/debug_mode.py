import asyncio

from concurrency.util.delay import delay
from concurrency.util.timer import async_timer


async def cpu_bound() -> int:
    c = 0
    for i in range(100000000):
        c += 1
    return c


@async_timer()
async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = 0.250

    t = asyncio.create_task(cpu_bound())
    loop.run_until_complete(t)


asyncio.run(main(), debug=True)
