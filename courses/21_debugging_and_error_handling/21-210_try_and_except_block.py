# handle errors!
# strongly encouraged to use try/except blocks

# lets define undefined variable
try:
    foobar
except:
    print("PROBLEM!")
print("after the try")

d = { "name": "Ricky" }

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d, 'city'))
