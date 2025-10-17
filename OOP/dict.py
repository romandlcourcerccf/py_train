class Sample:
    class_attr = 100
    def __init__(self, inst_attr):
        self.inst_attr = inst_attr

    def expose(self):
        print(f'class attr {self.class_attr}')
        print(f'class attr {self.inst_attr}')


inst = Sample(10)

print(Sample.__dict__['class_attr'])
print(inst.__dict__['inst_attr'])