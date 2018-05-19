# generators
# - generators are iterators
# - generators can be created with generator functions
# - generators functions use the yield keyword

# Functions                                 Generators Functions
# - uses return -                           uses yield
# - returns once -                          can yield multiple times
# - when invoked returns the return value   when invoked returns a generator

# example
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5) # this creates a generator object
next(counter)

for num in counter:
    print(num)