class Vectr:
    typecode = "d"


class MySeq:
    def __init__(self, l) -> None:
        self.l = l

    def __len__(self):
        return len(self.l)

    def __getitem__(self, i):
        return self.l[i]


ms = MySeq([1, 2, 3, 4])


print(ms[1:])
