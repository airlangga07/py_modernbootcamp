# iterator - an object that can be iterated upon. An object which retuns data, 
# one element at a time when next() is called on it

# iterable - an object which whill return an iterator when iter() is called on it.

# this is not an iterator, but it is iterable
name = "oprah" 

# to make it as an iterator and can be called with next(), we need to called iter()
it = iter(name) # this will return an iterator
next(it) # returns 'o'
next(it) # returns 'p', and so on..

# so we can call this
for c in it:
    print(c)

# NEXT, when next() is called on a itrator, the iterator returns the next item.
# it keeps doing so until it raises a StopIteration error
