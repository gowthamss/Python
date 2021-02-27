class Player:
    def __init__(self, name):
        self.name = name

    # A classmethod decorator is something which itself creates an instance called 'cls'
    # so that we do not have instantiate to execute the method
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # A staticmethod decorator is similar to the classmethod but it does not create any 'cls'
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


result = Player.adding_things(2, 3)
print(result)
result2 = Player.adding_things2(3, 4)
print(result2)
