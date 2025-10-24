from typing import Any
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'Vector ({self.x!r} , {self.y!r})'
    def __abs__(self):
        return math.hepot( self.x, self.y)
    
    def __bool__(self):
        return bool(math.hypot(self.x, self.y))

    def __add__(self, _other):
        return Vector(_other.x+self.x, _other.y+self.y)
    
    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)


v1 = Vector(1,2)
v2 = Vector(2,3)

print(v1 + v2)

print(bool(Vector(1,2)))
print(bool(Vector(0,0)))





