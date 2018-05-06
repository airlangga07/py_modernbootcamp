# clear will clear all the contents of dict
d = dict(a=1, b=2, c=3)
d.clear()
print(d) # {}

# copy will make a copy with difference object in the memory
d = dict(a=1, b=2, c=3)
c = d.copy()
c # {'a': 1, 'b': 2, 'c': 3}
print(c is d) # False

# fromkeys, creates key-value pairs from comma separated values
{}.fromkeys("a", "b") # { "a": "b" }
{}.fromkeys("a", [1, 2, 3, 4, 5]) # {'a': [1, 2, 3, 4, 5}

print({}.fromkeys(["name", "score", "email", "profile"], "unknown"))
# { 'name': 'unknown', 'score': 'unknown', etc }

# get, retrieves a key in an object and return None instead of a KeyError
d = dict(a=1, b=2, c=3)
d.get('a') # True
d.get('what') # None
