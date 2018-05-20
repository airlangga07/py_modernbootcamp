# decorators
# decorators are functions
# it wraps other functions and enhance their behaviour
# are examples of higher order functions
# it have their own sytax, using "@" 

# example
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    
    return wrapper

def greet():
    print("My name is Colt")

greet = be_polite(greet)
greet()

# we can use syntatic sugar of "@"
def be_polite2(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("have a great day!")
    
    return wrapper

@be_polite2 # this is equal to greet2 = be_polite2(greet2)
def greet2():
    print("My name is Mikael")

greet2()