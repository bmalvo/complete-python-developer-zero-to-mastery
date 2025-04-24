from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capi(item):
    return item.capitalize()

new_my_pets = list(map(capi, my_pets))
print(new_my_pets)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to 
# highest.

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

zip_items = zip(my_strings, my_numbers[::-1])
print(list(zip_items))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over(item):
    return item > 50

new_scores = filter(over, scores)
print(list(new_scores))

# 4 Combine all of the numbers that are in a list on this file using reduce 
# (my_numbers and scores). What is the total?

total_number = []
total_number.extend(my_numbers)
total_number.extend(scores)
print(total_number)

def acc(acc, item):
    return acc + item

total_reduce = reduce(acc, total_number, 0)

print(total_reduce)