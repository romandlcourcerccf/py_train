import functools
import time
from typing import Callable, Any


def async_timer():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Start func {func} ")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"Finish func {func} {total} ")

        return wrapped

    return wrapper
