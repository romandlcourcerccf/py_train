from collections.abc import Generator


def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0

    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


av = averager()
print(next(av))

print(av.send(10))
print(av.send(20))
print(av.send(30))
av.close()
av.close()
print(av.send(30))
