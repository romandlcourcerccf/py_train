# list_of_funcs = []

# def decorator(func):
#     list_of_funcs.append(func)
#     def inner(*args, **kwargs):
#         print('Call this func!')
#         func(*args, **kwargs)
#     return inner

# # @decorator
# # def func():
# #     print("I'm just func!")

# # print(func)

# @decorator
# def f1():
#     pass

# @decorator
# def f2():
#     pass

# @decorator
# def f2():
#     pass

# print('list_of_funcs ', list_of_funcs)

# import time

# def clock(func):
#     def clocked(*args):
#         t0 = time.perf_counter()
#         res = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_str = ','.join(repr(arg) for arg in args)
#         print(f'[{elapsed:0.8f} {name} ({arg_str}) -> {res}]')
#         return res
    
#     return clocked

# @clock
# def f(secs):
#     time.sleep(secs)

# f(3)


# import time
# import functools

# def clock(func):
#     def clocked(*args, **kwargs):
#         t0 = time.perf_counter()
#         res = func(*args, **kwargs)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_str = ','.join(repr(arg) for arg in args)
#         print(f'[{elapsed:0.8f} {name} ({arg_str}) -> {res}]')
#         return res
    
#     return clocked

# @clock
# def f(secs):
#     time.sleep(secs)

# f(3)


DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


import time
import functools

def clock(fmt = DEFAULT_FMT):
    def decorate(func):
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            _result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_str = ','.join(repr(arg) for arg in args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return result
        return clocked
    
    return decorate

@clock()
def f(secs):
    time.sleep(secs)

f(3)
