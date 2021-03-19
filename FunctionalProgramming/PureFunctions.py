# Pure Functions
# A Pure Function is a fuctions which follows 2 principles
#  1. Given the same input, it always produces same output
#  2. Does not produce any side effects

from functools import reduce


def multiplyBy2(li):
    new_list = []
    for item in li:
        new_list.append(item)
    return new_list


multiplyBy2([1, 2, 3])


# map, filter, zip, reduce

my_list = [1, 2, 3]

# map
# Iterates over the list and act upon each element and returns the modified list


def multiplyBy4(item):
    return item * 4


print(list(map(multiplyBy4, my_list)))
print(my_list)


# filter
# Iterates over the list and filters the item that did not satisfy the condition
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))


# zip
# Iterates over the given lists and creates single list containing sets of values from each iteration
your_list = [10, 20, 30]
print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]


# reduce
# Iterates over the list and return a single value recuding all the items
def reduce_array(acc, item):
    return acc + item


print(reduce(reduce_array, my_list, 0))


# Excercise

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.upper()


print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_scores(item):
    return item > 50


print(list(filter(filter_scores, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def reduce_numbers(acc, num):
    return acc + num


print(reduce(reduce_numbers, (my_numbers + scores), 0))


# Lambda Expressions
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression

# Rewriting all the map, filter, reduce functions defined above with lambda functions
print('map with lambda functions: ', list(map(lambda item: item * 2, my_list)))
print('filter with lambda functions: ', list(
    filter(lambda item: item % 2 != 0, my_list)))
print('reduce with lambda functions: ', reduce(
    lambda acc, item: acc + item, my_list))


# Excercise
# print sqListCuares using lambda
lambda_squares = [5, 4, 3]
print('Squares', list(map(lambda item: item ** 2, lambda_squares)))

# List sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(f'a: {a}')
