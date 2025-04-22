# OOP

# Encapsulation is bundling data and the methods that operate on that data 
# within a single unit, often a class, and restricting direct access to some 
# of the object's components.

# Abstraction focuses on showing only essential information and hiding complex 
# implementation details.

# Inheritance allows a new class to inherit properties and behaviors from an 
# existing class, establishing a relationship between them.

#  Polymorphism enables objects of different classes to be treated as objects 
# of a common type, allowing for flexible and reusable code.

# class player_character:
#     def __init__(self, name='unknown', age=0):
#         self.name = name
#         self.age = age

#     def run(self):
#         print('run')

#     def speak(self):
#         print(f'My name is {self.name}, and I am {self.age} years old')

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)


# player1 = player_character('Stefka', 15)
# player2 = player_character('Brydzia', 14)
# player3 = player_character()

# print(player1.name, player1.age)
# print(player2.name, player2.age)
# print(player3.name, player3.age)

# player1.speak()

# player4 = player_character.adding_things(2,3)

# print(player4.name, player4.age)

class User(object):
    def __init__(self,name, email='brak'):
        self.email = email
        self.name = name

    def sing_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(name,email)
        # self.name = name
        self.power = power

    def attack(self):
        print(f'attack with power of {self.power}')

    def __str__(self):
        print(f'{self.name} has a power: {self.power} and his emial is: {self.email}')

class Archer(User):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        # self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f'attakich with arrows: arrows left- {self.num_arrows}')
    

wizard1 = Wizard('Marlin', 50, 'wizwiz@hokus.com')
archer1 = Archer('Robin', 100)
wizard1.attack()
print(wizard1.email )
archer1.attack()
print(archer1.email)
# archer1.attack()
wizard1.__str__()

# def player_attack(character):
#     character.attack()

# player_attack(archer1)