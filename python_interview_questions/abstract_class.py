from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def my_method():
        ...


class B(A):
    def my_method(self):
        print("my_method")


B().my_method()
