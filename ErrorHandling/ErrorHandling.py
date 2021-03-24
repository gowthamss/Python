# Error Handling
def divide_by_zero():
    return 5 / 0


# divide_by_zero()


# Handling known and multiple exceptions
while True:
    try:
        age = int(input('Enter your age: '))
        print(10/age)
        if(age < 18):
            raise ValueError('Please verify that you are an adult')
    # except ValueError:
    #     print('Please enter a number')
    #     continue
    except ZeroDivisionError:
        print('Please enter a number other than 0')
        break  # Dont need to break here
    else:
        print('Thank you!')
        break
    finally:
        print('ok, I am finally done')
    print('can you hear me?')


def sum(num1, num2):
    return num1 + num2


print(sum('1', '2'))
