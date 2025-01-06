import os
import multiprocessing

def say_hello():
    print(f'hello from process! {os.getegid()}')


if __name__ == '__main__':

    print(f'hello from parent process! {os.getegid()}')

    process = multiprocessing.Process(target=say_hello)
    process.start()
    process.join()

