picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
] 

for row in picture:
    for num in row:
        if num == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')