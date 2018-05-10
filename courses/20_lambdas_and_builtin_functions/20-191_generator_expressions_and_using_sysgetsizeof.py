people = ['charlie', 'chrissy', 'christina', 'casey']

# this is generator object
# generator object uses () instead of list comprehension using []
print((name[0] == 'c' for name in people))

# proof that generator and list comprehension in performance
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof((x * 10 for x in range(1000)))

print("to do the same thing, it takes...")
print("List comprehension: {} bytes.".format(list_comp))
print("Generator expression: {} bytes.".format(gen_exp))
