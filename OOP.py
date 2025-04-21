# OOP

class player_character:
    def __init__(self, name='unknown', age=0):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)


player1 = player_character('Stefka', 15)
player2 = player_character('Brydzia', 14)
player3 = player_character()

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player3.name, player3.age)

player1.shout()

player4 = player_character.adding_things(2,3)

print(player4.name, player4.age)