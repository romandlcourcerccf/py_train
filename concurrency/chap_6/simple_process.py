import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    count = 0
    while count < count_to:
        count += 1
    print(f"It took {time.time() - start}")

    return count


if __name__ == "__main__":
    start_time = time.time()

    ps_1 = Process(target=count, args=(100000000,))
    ps_2 = Process(target=count, args=(100000000,))

    ps_1.start()
    ps_2.start()

    ps_1.join()
    ps_2.join()

    end_time = time.time()

    print(f"all in  {end_time - start_time}")
