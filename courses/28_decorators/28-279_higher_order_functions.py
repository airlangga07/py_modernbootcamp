# we can pass funcs as args to other funcs

def sum(n, func):
    total = 0
    for i in range(n):
        total += func(i)
    return total

def square(x):
    return x * x

def cube(x):
    return x * x * x

print(sum(10, square))
print(sum(10, cube))

# we can nest functions inside one another
from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello There ', 'Go Away ', 'I love you '))
        return msg
    
    result = get_mood() + person
    return result

print(greet('tony'))

# we can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHA', 'LOL', 'thehehe'))
        return l
    
    return get_laugh

laugh = make_laugh_func()
print(laugh())

# inner functions can access other function scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHA', 'LOL', 'thehehe'))
        return "{} {}".format(laugh, person)
    
    return get_laugh

laugh_at = make_laugh_at_func("linda")
print(laugh_at())