# object is the base class for every other class

# Parent class
class User():
    def sign_in(self):
        print('logged in')


# Child class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


# Child class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows. arrows left: {self.num_arrows}')

    def run(self):
        print('ran fast')


wizard1 = Wizard('Merlin', 50)
print(wizard1.sign_in())
wizard1.attack()

archer1 = Archer('Tim', 100)
archer1.attack()

# Checking instance
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))


# Multiple Inheritance
class HybridBord(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBord('borgie', 30, 40)
hb1.attack()
hb1.run()
hb1.sign_in()
