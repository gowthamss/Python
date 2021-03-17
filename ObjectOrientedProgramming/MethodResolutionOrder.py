# MRO - Method Resolution Order
class A:
    num = 10


class B:
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())
print(D.num)
