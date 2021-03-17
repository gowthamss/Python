class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


# Child class
class Wizard(User):
    def __init__(self, name, power, email):
        # Passing email to parent class
        # 1
        # User.__init__(self, email)
        # 2
        super().__init__(email)

        self.name = name
        self.power = power

    def attack(self):

        # Polymorphism, here we are calling the method of the parent class
        # with the same name as child class
        User.attack(self)
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
print(wizard1.attack())
print(wizard1.email)
