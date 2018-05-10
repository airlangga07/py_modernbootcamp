# Return filter object which can be converted into other iterables
# the object contains only the values that return true to the lambda

l = [1, 2, 3, 4, 5]

evens = filter(lambda x: x % 2 == 0, l)

for i in evens:
    print(i)
