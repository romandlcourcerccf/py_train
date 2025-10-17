import math


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value < 0:
            raise ValueError("Positive number expected!")

        instance.__dict__[self._name] = value


class Circle:
    def __init__(self, radius):
        self.radius = PositiveNumber()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value < 0:
            raise ValueError("Positive number expected!")

        self._radius = value

    def calc_area(self):
        return math.pi * self._radius**2


c1 = Circle(100)

print(c1.radius)

c2 = Circle(100)
