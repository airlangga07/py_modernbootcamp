# list comprehension
nums = [1, 2, 3]
new_nums = [x * 10 for x in nums]
print(new_nums)

# another example
name = 'colt'
chars = [char.upper() for char in name]
print(chars) # ['C', 'O', 'L', 'T']
