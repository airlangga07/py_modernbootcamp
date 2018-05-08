# scope

# 1. variables created in functions are scoped in that function!
instructor = 'Colt'

def say_hello():
    return "Hello {}".format(instructor)

say_hello() # 'hello colt'

# if you put it inside
def say_hello_2():
    instructor2 = 'hello'
    return "Hello {}".format(instructor2)

print(instructor2) # error

# global scope
total = 0
def increment():
    total += 1
    return total

# Error! because it tries to find local variable inside the increment()
# instead of using the global variable
increment() 

# you can do this by the way
def increment():
    global total
    total += 1
    return total

# nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


