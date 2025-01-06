# def subgen():
#     message = yield "Ready to accept :"

#     print("subgen received: ", message)


def corutine(fun):
    def inner(*args, **kwargs):
        g = fun(*args, **kwargs)
        g.send(None)
        return g

    return inner


class MyException(Exception):
    pass


@corutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except MyException:
            print("My exception")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average
