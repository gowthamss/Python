'''
my_file = open('text.txt')
print(my_file.read())
# The seek method is used because, python uses a concept of cursor,
# when it reaches the end of the content the cursor stays there
# so if we print the read method second time it returns empty spaces
# To set the cursor to the start positon, we use seek method
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())

print(my_file.readline())
print(my_file.readlines())

my_file.close()
'''

'''
# Standard way to read a file - we don't have to close the file
# mode = specifies the action (read, write, append, read-write). Default is 'read'

with open('text.txt', mode='r') as my_file2:
    print(my_file2.read())
'''

'''
# mode(r+) = reads and writes the data
# This mode sets the cursor to the start, so the written text starts from the beginning

with open('text.txt', mode='r+') as my_file2:
    print(my_file2.write(':)'))
'''

'''
# mode(w) = writes the data to the file(overwrites the data)
# If there is no file exists, it creates a new file
with open('text.txt', mode='w') as my_file2:
    print(my_file2.write(':)'))
'''

'''
# mode(a) = append the data to the existing data
with open('text.txt', mode='a') as my_file2:
    print(my_file2.write(':)'))
'''

'''
# Reading file paths
with open('../Debugging/debugging.py', mode='r') as my_file2:
    print(my_file2.read())
'''

'''
# File IO errors
try:
    with open('test.txt') as my_file2:
        print(my_file2.read())
except FileNotFoundError:
    print('File does not exist')
'''

# Python package to work - pathlib


# Excercise: Translator

from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('text.txt') as trans:
        japan = trans.read()
        translation = translator.translate(japan)
        print(translation)
except FileNotFoundError:
    print('File not found, check your file path')
except IOError as err:
    print(err)
