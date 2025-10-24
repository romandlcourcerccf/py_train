def factorial(n):
    """
        returns n!
    """
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))
print(factorial.__doc__)

f = factorial

print(list(map(factorial, range(10))))


