# we can use any loops to iterate over a tuple just like a list
nums = (1, 2, 3, 4)

for num in nums:
    print(num)

# tuple methods: count
x = (1, 2, 3, 3, 3)
x.count(3) # 3
x.count(1) # 1

# tuple methods: index, returns the index at which a value is found in a tuple
t = (1, 2, 3, 3, 3)
t.index(1) # 0
t.index(5) # ValueError
t.index(3) # 2, only first matching index
