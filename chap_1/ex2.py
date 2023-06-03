import os
import threading

def hello_from_thread():
    print('Hell0')

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Total threads running {total_threads}')
print(f'Current thread name is {thread_name}')

hello_thread.join()


