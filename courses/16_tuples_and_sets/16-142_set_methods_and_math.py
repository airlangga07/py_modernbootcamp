# add(), will adds an element to a set
s = {1, 2, 3}

s.add(4)
s.add(4) # adding add again will not affect anything, no error but not gets added.

# remove(), removes a value form the set
s.remove(3) # {1, 2, 4}
s.remove(3) # KeyError

# use discard() if you do not want to get an error
s.discard(3) # None

# copy() makes a copy of that set, but not identical in memory

another_s = s.copy()

# clear() removes all the content of the set
another_s.clear()

# SET MATH
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# union will combine both sets and removes duplicate
print(math_students | biology_students)

# intersection will return value that shared between two set
print(math_students & biology_students)
