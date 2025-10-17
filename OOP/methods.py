class ObjectCounter:
    instanses = 0
    def __init__(self):
        type(self).instanses +=1
    

insts = [ ObjectCounter() for i in range(10)]

insts[0].instanses=20
ObjectCounter.instanses = 20

print(insts[0].instanses)
print(ObjectCounter.instanses)