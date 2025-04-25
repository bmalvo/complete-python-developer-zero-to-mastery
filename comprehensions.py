number_list = [x for x in range(10)]

print(number_list)

string_list = [char for char in 'hello']

print(string_list)

even_numbers = [num for num in range(101) if not num % 2]

print(even_numbers)

# dictionary comprehension

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}

print(my_dict)

second_dict = {num: num*2 for num in [1,2,3]}

print(second_dict)

# exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({char for char in some_list if some_list.count(char) > 1})

print(duplicates)