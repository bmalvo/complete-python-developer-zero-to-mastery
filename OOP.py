# OOP

class player_character:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = player_character('Stefka', 15)
player2 = player_character('Brydzia', 14)

print(player1.name, player1.age)
print(player2.name, player2.age)
