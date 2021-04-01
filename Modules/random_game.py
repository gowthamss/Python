import random
from sys import argv

# Reac command line arguments which is start and end range
start = int(argv[1])
end = int(argv[2])
while True:
    try:
        g_number = int(input('Guess a number 1 ~ 10: '))
        # Generate a random number
        random_number = random.randint(start, end)
        # Check if the input is equal to random number
        if random_number == g_number:
            print('You rock!')
            break
    except ValueError:
        print('Please enter a number')
    # If not keep them guessing
    else:
        print('You have got this, keep trying...')
