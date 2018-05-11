# try:
# except:
# else:
# finally:

while True:
    try:
        num = int(input('please enter a number: '))
    except:
        print('that is not a number!')
    else:
        print('i am in the else.')
    finally:
        print('runs no matter what')
print('Rest of the game logic runs!')

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('do not divide by zero please')
    except TypeError as err:
        print('a and b must be ints or floats')
        print(err)
    else:
        print(result)

print(divide(1, 2))
print(divide(1, 0))
