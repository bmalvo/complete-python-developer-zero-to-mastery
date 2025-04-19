# functions (DRY)
# parameters


# def say_hello(name='unknown', emoji='🍕'):
#     return f'Heellooo {name}!{emoji}'


# print(say_hello('Stefka', '🚀'))
# print(say_hello('Brydzia'))

# print("".join(['a','b','c']))

evens = [6, 10, 2, 3, 4, 8, 11]

def highest_even(data):
    '''output highest even number from data'''
    highest = [num for num in data if num % 2 == 0]
    return max(highest)

print(highest_even(evens))
