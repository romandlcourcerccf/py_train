def corutine(fun):
    def inner(*args, **kwargs):
        g = fun(*args, **kwargs)
        g.send(None)
        return g

    return inner


class GenException(Exception):
    pass


# @corutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print("Got GenException")
            break
        else:
            print("........", message)

    return "Value from subgen"


@corutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except GenException as ge:
    #         g.throw(ge)

    result = yield from g
    print(result)
