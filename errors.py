# Errors

try:
    print([3 + 'wow!'])
except:
    print('something goes wrong')

while True:
    try:
        age = int(input('What is Your name? '))
        print(age)
    except:
        print('please enter a number')
    else:
        print('thank You!')
        break