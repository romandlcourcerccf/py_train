class A:
    def __init__(self, a) -> None:
        print("--> A")
        self.a = a


class B(A):
    def __init__(self, a, b) -> None:
        print("--> B")
        super(B, self).__init__(a)
        self.b = b


# B(1, 2)

# class C:
#  def __init__(self, a):
#    self.__a = a

# print(C(1)._C__a)

# class D:

#    def __new__(cls, a):
#       print('-->new-->')

#    def __init__(self, a) -> None:
#       print('-->init-->')
#       self.a = a

# D(1)\
