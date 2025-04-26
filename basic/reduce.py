from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,0]

def acc(acc, item):
    return acc + item

print(reduce(acc,my_list,0))