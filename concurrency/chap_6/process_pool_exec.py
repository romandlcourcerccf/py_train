import time

from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    count = 0
    while count < count_to:
        count += 1
    print(f"It took {time.time() - start}")

    return count


if __name__ == "__main__":
    with ProcessPoolExecutor() as pp:
        nums = [1, 3, 5, 22, 100000000]
        for result in pp.map(count, nums):
            print(result)
