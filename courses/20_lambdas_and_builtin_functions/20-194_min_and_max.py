# max, return the largest item in an iterable or the largest of two or more args
# we can pass in list, iterable
# min will have the same effect but searched for the minimum value

print(max(2, 45, 66)) # 66
print(max('c', 'd', 'a')) # 'd'
print(max([1, 2, 3, 4, 5])) # 5
print(max('hello world')) # 'w'

# another example
names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

min(names) # Arya
max(names) # Tim
min(len(name) for name in names) # 3

max(names, key=lambda x: len(x)) # Ollivander
min(names, key=lambda x: len(x)) # Tim

