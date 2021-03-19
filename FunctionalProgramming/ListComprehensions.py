# list comprehensions
# List comprehensions are shorthand syntax for creating a list of items

# Creating and appending items to the list by using for loop and append method
my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)

# Shortening the above code by using list comprehensions
my_list2 = [char for char in 'hello']
print(my_list2)

# Excercise:
my_list3 = [num for num in range(10)]
print(my_list3)

my_list4 = [num*2 for num in range(10)]
print(my_list4)

my_list5 = [num**2 for num in range(10) if num % 2 == 0]
print(my_list5)


# set , dictionary comprehensions
my_set = {char for char in 'hey there'}
print(my_set)


sample_dict = {'a': 1, 'b': 2}
# Grab the key value pairs from the dictionary and check if the value is divisible by 2
# if yes, store the key value pairs in the 'my_dict'
my_dict = {k: v**2 for k, v in sample_dict.items() if v % 2 == 0}
print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)


# Excercise: Find duplicates in a list using comprehensions
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
without_duplicates = list({char for char in [
    char for char in some_list if some_list.count(char) > 1]})
print(without_duplicates)
