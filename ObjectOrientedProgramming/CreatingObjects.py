# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    # Constructor

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            # if (self.membership):
            # Properties
            self.name = name
            self.age = age

    def run(self, speed):
        return f'I run {speed}'

    def shout(self, hello):
        return f'{hello} my name is {self.name}'


player1 = PlayerCharacter('Gowtham', 24)
player2 = PlayerCharacter('ss', 42)
player2.attack = 'fire'

print(player1.name, player1.age, player1.shout('hello,'), player1.run('fast'))
print(player2.name, player2.age, player2.attack)
