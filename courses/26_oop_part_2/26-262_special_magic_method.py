from copy import copy

# special method example
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return "Human named {} {}".format(self.first, self.last)
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that!"
    
    def __mul__(self, other):
        if isinstance(other, int):
            # create new copy of the current object and returns it
            return [ copy(self) for i in range(other) ]
        return "Cant multiply"
    
j = Human("Jenny", "Larsen", 78)
k = Human("Kevin", "Jones", 67)

# special method
print(len(j))
print(j + k)
print(j * 2)