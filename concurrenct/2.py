import asyncio
from time import time


async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)


# async def main():
#     task1 = asyncio.create_task(print1())
#     task2 = asyncio.create_task(print2())
#     task3 = asyncio.create_task(print3())

#     await asyncio.gather(task1, task2, task3)

# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(print1())
#         tg.create_task(print2())
#         tg.create_task(print3())


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))


start = time()
asyncio.run(main())

print(f"Total time is {time() - start}")
