import os
import threading

print(f'Process id {os.getpid()}')

tot_threads = threading.active_count()
th_name = threading.current_thread().name

print(f'tot_threads : {tot_threads}')
print(f'current thread :{th_name}')