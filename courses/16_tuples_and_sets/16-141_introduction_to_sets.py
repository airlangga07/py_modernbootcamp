# Sets
# sets are like formal mathematical sets
# sets do not have duplicate values
# elements in sets aren't ordered
# you cannot access items in a set by index

# creating
s = set({1, 2, 3, 4, 5})
# or
another_s = {1, 3, 4}
print(3 in another_s) # True

# accessing all values in a set using a loop
for val in s:
    print(val)

# common use case, is that we have a list that might have duplicate
# and we want to create a unique list of element
cities = ["Singapore", "Jakarta", "New York", "Singapore", "Jakarta", "Surabaya"]
print(set(cities)) # Singapore, Jakarta, New York, Surabaya
# you can count it too
print(len(set(cities)))
