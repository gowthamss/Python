# Generators hold the current item in the loop in memory and clears it when the iteration is done.
# While, if we use a list to iterate, the engine needs to store the entire list in the memory.
# So, generators are efficient than looping over a list.

# Example:
# Performance Decorator
from time import time


def performance(fn):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        time_diff = t2 - t1
        print(f'The program took {time_diff}ms')
        if(time_diff < 2):
            print('Your program performed quite well!')
        elif(time_diff < 5):
            print('You could do a bit better!')
        else:
            print('Bad. You really need to look at your code to optimize it.')

        return result
    return wrapper_func


@performance
def long_time():
    print('1')
    for i in range(10000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i * 5


# long_time()
# long_time2()


# Creating a Generator
def gen_func(num):
    for i in range(num):
        yield i


# for i in gen_func(100):
#     print(i)


def fibonacci(number):
    f1 = 0
    f2 = 1
    for i in range(number):
        f3 = f1
        print(f3)
        f1 = f2
        f2 = f3 + f1


fibonacci(20)
