import time
import os


def clock():
    time0 = round(time.time())
    while True:
        if round(time.time() - time0) % 5 == 0:
            yield "5 sec"
        else:
            yield 0


def query():
    for i in os.walk("/Users/mac/py_projects"):
        yield i[0]


def main():
    deta = query()
    alarm = clock()

    while True:
        d = next(deta)
        a = next(alarm)

        print(d)
        if a:
            print(a)
        time.sleep(1)


main()
