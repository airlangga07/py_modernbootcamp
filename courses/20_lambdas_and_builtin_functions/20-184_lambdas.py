# normal function
def square(num): return num * num
print(square(9))

# lambda function
square2 = lambda num: num * num
print(square2(9))

# another lambda function
add = lambda a, b: a + b
print(add(2, 4))
print(add.__name__) # <lambda>
