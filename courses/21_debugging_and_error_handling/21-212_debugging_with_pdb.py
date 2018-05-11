# debugging with pdb
import pdb

first = 'First'
second = 'Second'

# see the variable
pdb.set_trace()

result = first + second
third = 'Third'
result += third
print(result)

# pdb gotcha
def add_numbers(a, b, c, d):
    # you usually use it like this, do not import it 
    # at the top of the file
    import pdb; pdb.set_trace()

    return a + b + c + d

print(add_numbers(1, 2, 3, 4))
