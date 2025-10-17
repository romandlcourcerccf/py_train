import functools
import time


def my_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        func(*args, **kwargs)
        print(time.perf_counter() - s)

    return wrapper


@my_deco
def my_func():
    pass


my_func()
