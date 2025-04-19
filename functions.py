# functions (DRY)
# parameters


def say_hello(name='unknown', emoji='🍕'):
    return f'Heellooo {name}!{emoji}'


print(say_hello('Stefka', '🚀'))
print(say_hello('Brydzia'))

print("".join(['a','b','c']))