from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f"Hey there {name}"


if __name__ == "__main__":
    with Pool() as process_poll:
        pp1 = process_poll.apply_async(say_hello, args=("Roman",))
        pp2 = process_poll.apply_async(say_hello, args=("Ivan",))

        print(pp1.get())
        print(pp2.get())
