# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Stefka', 15)
cat2 = Cat('Brydzia', 14)
cat3 = Cat('Ninja', 5)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldest_cat = find_oldest_cat([cat1, cat2, cat3])
print(f'The oldest cat is {oldest_cat.age} years old.')