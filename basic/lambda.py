my_list = [1,2,3,4,5]

print(list(map(lambda item: item * 2, my_list)))

# square
power_list = [5,4,3]

print(list(map(lambda num: num * num, power_list)))

#  list sorting

a = [(0,2), (4,3), (9,9), (10, -1)]

a.sort(key=lambda i: i[-1])

print(a)