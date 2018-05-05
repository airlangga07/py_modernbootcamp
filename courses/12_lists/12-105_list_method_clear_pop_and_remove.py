# clear() clears everything
items = [1, 2, 3, 4]
items.clear()
print(items)

# pop() remove one item from the array
first_list = [1, 2, 3, 4]
first_list.pop() # 4
first_list.pop(1) # 2
print(first_list)

# remove() remove the first item from the list whose value is x
items = [1, 2, 3, 4, 4, 4]
items.remove(2)
print(items) # [1, 3, 4, 4, 4]
items.remove(4)
print(items) # [1, 3, 4, 4]
