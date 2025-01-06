import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds have passed")
        count += 1
        await asyncio.sleep(1)


async def main():
    task_1 = asyncio.create_task(print_nums())
    task_2 = asyncio.create_task(print_time())

    await asyncio.gather(task_1, task_2)


if __name__ == "__main__":
    asyncio.run(main())
