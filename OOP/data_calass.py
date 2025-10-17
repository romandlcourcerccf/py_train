from dataclasses import dataclass


@dataclass
class MyDataClass:
    x: int | float
    y: int | float
    z: int | float

    @classmethod
    def get_instance(cls, seq):
        return cls(*seq)

    @classmethod
    def expose(cls, mes):
        print(f"point : {mes}")


inst1 = MyDataClass.get_instance([1, 2, 3])

print(inst1)
