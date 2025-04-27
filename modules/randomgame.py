from random import randint
import sys

min = sys.argv[1]
max = sys.argv[2]

# generate a number 1-10
answer = randint(int(min), int(max))
print(answer)
# print(answer)
#  input from user

# check that input is a number 1-10
while True:
    try:
        guess = int(input(f'guess a number {min}-{max}'))
        if  int(min) -1 < guess < int(max) +1:
            if guess == answer:
                print('You are wright!')
                break
        else: 
            print(f'number from {min} to {max}')
    except ValueError:
        print('please enter a number')
        continue

# check if number is the right guess, otherwise ask again
