def exponent(num, power=2):
    return num ** power

print(exponent(2, 3)) # 8
print(exponent(3)) # 9
print(exponent(7)) # 49

# you can pass function in parameters too
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def math(a, b, fn=add):
    return fn(a, b)

print(math(1, 2))
print(math(3, 2, subtract))
