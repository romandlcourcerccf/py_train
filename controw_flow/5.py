import re
import reprlib

REG_WORD = re.compile(r"\w+")


class Sequence:
    def __init__(self, text):
        self.text = text
        self.words = REG_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in REG_WORD.finditer(self.text))


for s in Sequence("ww ww dcvd vvf"):
    print(s)

# s1 = Sequence("aa aa")

# it = iter(s1)

# print(next(it))
# print(next(it))
# print(next(it))


# def gen3():
#     yield 1
#     yield 2
#     yield 3


# g = gen3()
# print(dir(g))
