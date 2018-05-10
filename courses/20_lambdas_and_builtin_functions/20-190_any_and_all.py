# all -> return True if all elements of the iterable are truthy

all([0, 1, 2, 3]) # False

all([char for char in 'eio' if char in 'aeiou']) # True

all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]) # True

people = ['charlie', 'casey', 'cody', 'carly', 'cristina']
all([ name[0] == 'c' for name in people ])

# any -> return True if any element of the iterable is truthly

all([0, 1, 2, 3]) # True

nums = [2, 60, 26, 18, 21]

any([ num % 2 == 1 for num in nums ]) # True
