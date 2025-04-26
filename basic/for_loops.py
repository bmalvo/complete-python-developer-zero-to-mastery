#/ for loops
 
# for num in (1,2,3,4,5):
#     print(num)

# print(num)

# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for k, v in user.items():
#     print(k, v)

# for numb in range(101):
#     if numb % 3 == 0:
#         print(numb)

# while loop

# i = 0

# while i < 10:
#     print(i)
#     i += 1
print('test')

my_list = [1,2,3,'something',4,5,6]

i = 0

while i < len(my_list):
    if type(my_list[i]) == str:
        i += 1
        continue
    print(my_list[i])
    i += 1
