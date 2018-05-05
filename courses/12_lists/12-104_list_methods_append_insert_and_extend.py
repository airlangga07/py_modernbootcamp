nums = [1, 2, 3]
print(len(nums))

nums.append([4, 5])
print(nums)

# extends
nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)

# insert, insert an item at given position
first_list = [1, 2, 3, 4]
first_list.insert(2, 'hi!')
print(first_list)
