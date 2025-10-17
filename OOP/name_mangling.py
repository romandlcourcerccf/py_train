class Mangler:
    def __init__(self, val):
        self.__val = val

    def __expose(self):
        print(self.__val)


inst = Mangler(10)

print(vars(inst))

print(inst._Mangler__expose())

print(inst._Mangler__val)

