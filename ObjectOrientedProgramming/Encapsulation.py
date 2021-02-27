# Encapsulation means binding the data and the methods together
class Player:
    def __init__(self, name, age):
        # Properties
        self.name = name
        self.age = age

    # Methods
    def run(self):
        return 'fast'

    def speak(self):
        print(
            f'My name is {self.name} and I\'m {self.age} years old, I run {self.run()}. ')


player1 = Player('Gowtham', 24)
print(player1.speak())
