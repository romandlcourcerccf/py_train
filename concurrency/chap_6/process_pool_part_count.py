import time
import asyncio
import concurrent.futures

from collections import defaultdict
from typing import List, Dict
import functools

freqs = defaultdict(int)


def partition(data: List, chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def map_freqs(chunks: List[str]) -> Dict[int, int]:
    counter = defaultdict(int)

    for line in chunks:
        word, _, count, _ = line.split()
        counter[word] += int(count)

    return counter


def merge_dicts(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    return {**first, **second}


async def reduce(loop, pool, counters, chunk_size):
    chunks: List[List[Dict]] = list(partition(counters, chunk_size))
    reducers = []

    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = functools.partial(functools.reduce, merge_dicts, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))

        reducer_chunks = await asyncio.gather(*reducers)
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()

    return chunks[0][0]


async def main(part_size: int):
    with open(
        "/Users/roman/Downloads/googlebooks-eng-all-1gram-20120701-a", "r"
    ) as reader:
        lines = reader.readlines()
        loop = asyncio.get_running_loop()
        tasks = []

        loop = asyncio.get_running_loop()

        start = time.time()
        with concurrent.futures.ThreadPoolExecutor() as pool:
            for chunk in partition(lines, part_size):
                tasks.append(
                    loop.run_in_executor(pool, functools.partial(map_freqs, chunk))
                )

            intermediate_results = await asyncio.gather(*tasks)
            final_result = await reduce(loop, pool, intermediate_results, 500)

            print(f"Aardvark has appeared {final_result['Aardvark']}")

        print(f"{time.time() - start: .4f}")


if __name__ == "__main__":
    asyncio.run(main(part_size=6000))
