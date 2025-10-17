import asyncio

from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List


def count(count_to: int) -> int:
    count = 0
    while count < count_to:
        count += 1

    return count


async def main():
    with ProcessPoolExecutor() as pp:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 100000000]
        calls: List[partial[int]] = [partial(count, num) for num in nums]

        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(pp, call))

        ress = await asyncio.gather(*call_coros)

        for res in ress:
            print(res)
