from time import time

# Higher Order Functions
# A HOC is a function which either takes a function as a parameter or returns a function


def greet(func):
    func()


def hello():
    def func():
        return 5
    return func

# Decorators
# Decorators super charge out functions(add extra featurs/functionality)
# Decorators are really useful when we want to add extra functionality to normal functions
# They receive a function as a parameter and wraps it inside another function,
# in which we can have extra functionality, and return that function as a whole.

# Defining own decorator


def my_decorator(func):
    def wrapper_func(*args, **kwargs):
        print('*' * 10)
        func(*args, **kwargs)
        print('*' * 10)
    return wrapper_func


@my_decorator
def greet_user(name, emoji):
    print(f'Hello {name} {emoji}, good to see you here')


greet_user('Gowtham', ':)')


# Creating performance decorator which gives how fast out code runs
# Packages needed: time
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
    for num in range(100000):
        num * 5


long_time()

# Creating authentication decorator which only allows if the user is valid
user1 = {
    'name': 'Raj',
    'valid': False
}


def authenticated(fn):
    def wrapper_func(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result

    return wrapper_func


@authenticated
def message_friends(user):
    if user['valid']:
        print('Message has been sent')
    else:
        print('Not authenticated, try again.')


message_friends(user1)
