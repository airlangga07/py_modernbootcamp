# pop takes a single argument corresponding to a key and removes that key-value pair
d = dict(a=1, b=2. c=3)
d.pop('a')
d # { 'c': 3, 'b': 2)
d.pop('e') # KeyError

# popitem removes a random key-value pair from a dictionary
# popitem takes no argument, and returns the key-value pair
d.popitem()

# update keys and values in a dictionary with a another set of key-value pairs
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second) # { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

# lets try to overwrite an existing key
second['a'] = "AMAZING"

# if we update again
second.update(first) # { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

# the update overrides our value
print(second) # { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
