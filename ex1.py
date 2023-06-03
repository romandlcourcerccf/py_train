import os
import threading

print(f'pythoon process running with process id {os.getpid}')

local_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Local threads {local_threads}')
print(f'Current thread name {thread_name}')




