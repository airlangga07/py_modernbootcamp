# assertions with assert keyword
# assert accepts an expression

# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# print(add_positive_numbers(1, 1))
# add_positive_numbers(-1, 1)

def eat_junk(food):
    assert food in ['pizza', 'ice cream', 'candy', 'fried butter'], "food must be a junk food!"
    return "nom nom nom i am eating food.".format(food)

food = input('enter a food please: ')
print(eat_junk(food))