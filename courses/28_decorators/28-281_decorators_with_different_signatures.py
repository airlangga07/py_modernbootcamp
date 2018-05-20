# this is not good design because we do not consider all the arguments passed in
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, *kwargs).upper()
    return wrapper

@shout
def greet(name):
    return "Hi, I am {}".format(name)

@shout
def order(main, side):
    return "Hi, i'd like the {}, with a side of {}, please.".format(main, side)

@shout
def lol():
    return "lol"

print(greet('Todd'))
print(order('burger', 'fries'))
print(lol())