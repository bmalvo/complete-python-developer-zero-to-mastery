from utility import multiply
from shoping.shoping_cart import buy
from random import random,randint,shuffle, choice

print(multiply(2,3))

print(buy('apple'))

print(random())
print(randint(0, 10))
print(choice([1,2,3,4,5,6,7,8,9,0]))

my_list = ['a','b','c','d','e','f']

shuffle(my_list)

print(my_list)