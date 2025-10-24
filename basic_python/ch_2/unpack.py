a, b, *c = range(5)

print(a, b, c)

def f(a,b, c, *r):
    print('a: ',a)
    print('b: ',b)
    print('c: ',c)
    print('r: ',r)


print(f(*[1,2], 2, *range(10) ))

