# There are several errors in python

# SyntaxError -> incorrect syntax, usually due to typos
def first;;

# NameError -> variable is not defined or hasn't been assigned yet
test

# TypeError -> an operation or function is applied to the wrong type
len(5)
'awesome' + []

# IndexError -> access an element in a list using an invalid index
lista = ['hello']
lista[1]

# ValueError -> built-in operation or function receives an arg that has the 
# right type but inappropriate value
int('foo')

# KeyError -> when a dict does not have a specific key
d = {}
d['foo']

# AttributeError -> when a variable does not have an attribute
'awesome'.foo
