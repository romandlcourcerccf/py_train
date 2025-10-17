class User:
    """ """


jane = User()

jane.name = "Jane Doe"
jane.job = "Data Enginear"

print(jane.__dict__)


def __init__(self, name, job):
    self.name = name
    self.job = job


User.__init__ = __init__

linda = User("Linda", "gardener")

print(linda.__dict__)
