import os
import threading

def say_hello():
    print('Hello!')


new_thread = threading.Thread(target=say_hello)
new_thread.start()

tot_threads = threading.active_count()
th_name = threading.current_thread().name

print(f'tot_threads : {tot_threads}')
print(f'current thread :{th_name}')

new_thread.join()



