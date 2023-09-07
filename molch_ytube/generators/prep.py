
# def gen(s):
#     for i in s:
#         yield i

# g = gen('roman')

# from time import time

# def gen_filename():
#     while True:
#         pattern = 'file-{}.jpeg'
#         t = int(time() * 1000)
#         yield pattern.format(str(t))

#         sum = 123 * 123

#         print(sum)


def gen(s):
    for i in s:
        yield i


def gen_2(n):
    for i in range(n):
        yield i

g1 = gen('roma')
g2 = gen_2(4)

tasks = [g1, g2]
while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass


    