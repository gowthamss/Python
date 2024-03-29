class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


# Child class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):

        # Polymorphism, here we are calling the method of the parent class
        # with the same name as child class
        User.attack(self)
        print(f'attacking with power of {self.power}')


# Child class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows. arrows left: {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
print(wizard1.attack())


# Excercise
class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Billy(Cat):
    def sing(self, sounds):
        return f'{sounds}'


my_cats = [Simon('Simon', 3), Sally('Sally', 4), Billy('Billy', 5)]
my_pets = Pets(my_cats)
print(my_pets.walk())
