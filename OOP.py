# OOP
# Encapsulation is bundling data and the methods that operate on that data within a single unit, often a class, and restricting direct access to some of the object's components.
# Abstraction focuses on showing only essential information and hiding complex implementation details.

class player_character:
    def __init__(self, name='unknown', age=0):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name}, and I am {self.age} years old')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)


player1 = player_character('Stefka', 15)
player2 = player_character('Brydzia', 14)
player3 = player_character()

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player3.name, player3.age)

player1.speak()

player4 = player_character.adding_things(2,3)

print(player4.name, player4.age)