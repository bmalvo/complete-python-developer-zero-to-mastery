# generators
# range is a ganerator
#  all generators are iterable

range(100)
list(range(100))

def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(100)

next(g)
next(g)
print(next(g))

