# normal nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for l in nested_list:
    for val in l:
        print(val)

# nested list with list comprehension
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

xox = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(xox) # [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
