import re
import reprlib

REG_WORD = re.compile(r"\w+")


class Sequence:
    def __init__(self, text):
        self.text = text
        self.words = REG_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


for s in Sequence("ww ww dcvd vvf"):
    print(s)

s1 = Sequence("aa aa")

it = iter(s1)

print(next(it))
print(next(it))
print(next(it))
