# Errors

# try:
#     print([3 + 'wow!'])
# except:
#     print('something goes wrong')

# while True:
#     try:
#         age = int(input('What is Your name? '))
#         print(age)
#     except:
#         print('please enter a number')
#     else:
#         print('thank You!')
#         break

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         return f'please enter a number {err}'

# print(sum('1', 2))

while True:
    try:
        age = int(input('What is Your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number higher than 0')
    else: 
        print('thank You!')
        break
    finally:
        print('ok, i am finally done.')