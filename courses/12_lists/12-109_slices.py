# slicing: start
first_list = [1, 2, 3, 4]
first_list[1:] # [2, 3, 4]
first_lsit[3:] # [4]

# using negative value
first_list[-1:] # [4]
first_list[-3:] # [2, 3, 4]

# slicing: end
first_list[:2] # [1, 2]
first_list[:4] # [1, 2, 3, 4]
first_list[1:3] # [2, 3]

# using negative value
first_list[:-1] # [1, 2, 3]
first_list[1:-1] # [2, 3]

# slicing: step
first_list = [1, 2, 3, 4, 5, 6]
first_list[1::2] # [2, 4, 6]
first_list[::2] # [1, 3, 5]

# with negative numbers, reverse the order
first_list[1::-1] # [2, 1]
first_list[:1:-1] # [6, 5, 4, 3]
first_list[2::-1] # [3, 2, 1]

# tricks with slices
# reversing list / strings
string = 'This is fun!'
print(string[::-1])

# modifying portions of lists
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']
print(numbers) # [1, 'a', 'b', 'c', 5]
