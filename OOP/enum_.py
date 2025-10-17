from enum import Enum


class AgeCategory(Enum):
    YOUNG = 1
    MIDDLE = 2
    OLD = 3

    def __str__(
        self,
    ):
        return f"Age {self.name}"


o = AgeCategory.OLD

print(o)
print(AgeCategory["YOUNG"])
print(AgeCategory(2))
