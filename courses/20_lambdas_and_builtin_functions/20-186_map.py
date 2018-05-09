# map
# a standard function that accepts at least two args
# 1. a function
# 2. an iterable

nums = [1, 2, 3, 4, 5]

doubles = map(lambda x: x ** 2, nums)

people = ['darcy', 'christina', 'dana', 'annabel']

peeps = map(lambda x: x.upper(), people)
