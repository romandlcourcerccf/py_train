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
        return SequenceIterator(self.words)


class SequenceIterator:
    def __init__(self, words) -> None:
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


for s in Sequence("ww ww dcvd vvf"):
    print(s)

# s1 = Sequence("aa aa")

# it = iter(s1)

# print(next(it))
# print(next(it))
# print(next(it))
