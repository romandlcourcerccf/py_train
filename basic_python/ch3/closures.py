# class Averager():

#     def __init__(self):
#         self.series = []

#     def __call__(self, val):
#         self.series.append(val)
#         return sum(self.series)/ len(self.series)
    

# c = Averager()

# print(c(10))
# print(c(20))
# print(c(30))


# def make_averager():
#     series = []

#     def averager(new_val):
#         series.append(new_val)
#         return sum(series)/ len(series)
    
#     return averager

# avg = make_averager()

# print(avg(10))
# print(avg(20))
# print(avg(30))

def make_averager():
    count = 0
    total = 0

    def averager(val):
        nonlocal count, total
        count +=1
        total += val
        return total / count
    
    return averager
    
avg = make_averager()
print(avg(10))


print(__builtins__)



