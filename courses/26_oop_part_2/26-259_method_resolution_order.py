# whenever you create a class, Python sets a Method Resolution Order, 
# for that class, which is the order in which Python will look for methods
# on instance of that class

# you can programmatically reference the MRO three ways:
# - __mro__ attribute on the class
# - use mro() method on the class
# - use builtin help(cls) method

# Example, take a look at this diagram and its implementation
#    A
#  /   \
# B     C
#  \   /
#    D

class A:
    def do_something(self):
        print("method defined in : A")

class B(A):
    pass
    # def do_something(self):
    #     print("method defined in : B")

class C(A):
    def do_something(self):
        print("method defined in : C")

class D(B, C):
    pass
    # def do_something(self):
        # print("method defined in : D")

print(D.__mro__)
print(D.mro())
print(help(D))
# thing = D()
# thing.do_something()
