from functools import wraps


def mydecor(fun):
    @wraps(fun)
    def wrap(*args, **kwargs):
        print("mydecor")
        res = fun(*args, **kwargs)
        return res

    return wrap


def mydecor_with_arg(par=1):  
    print("par :", par)

    def mydecor(fun):
        @wraps(fun)
        def wrap(*args, **kwargs):
            print("mydecor")
            res = fun(*args, **kwargs)
            return res

        return wrap

    return mydecor


@mydecor
def myfunc_1():
    print("myfunc")


@mydecor_with_arg(2)
def myfunc_2():
    print("myfunc")


print(myfunc_1)
print(myfunc_2)
