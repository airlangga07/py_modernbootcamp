# Tuple is similar like list, except its immutable
alphabet = ('a', 'b', 'c', 'd')
print(alphabet)
alphabet.append('e') # 'tuple' has no attribute append
alphabet[0] = 'A' # 'tuple' does not support item assignment

# why tuple?
# tuple are faster
# it make your code safer
# acts as a valid keys in dict

# example
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul')
print(months[1]) # "Feb"

# tuples as key in dict
locations = {
    (23.44, 34.234): "Tokyo Office",
    (54.98, 52.343): "New York Office"
}

locations[(54.98, 52.343)] # "New York Office"
