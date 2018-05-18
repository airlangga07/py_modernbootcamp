# Polymorphism
# a key principle in OOP is the idea of an object can take on many (poly) forms (morph)

# Example
# 1. the same class method works in a similar way for different classes
# Polymorphism and Inheritance: use method overriding
class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

Cat.speak() # meow
Dog.speak() # woof
Animal.speak() # error

# 2. the same operation works for different kinds of objects
# use special method
# sample_list = [1, 2, 3]
# sample_tuple = (1, 2, 3)
# len(sample_list)
# len(sample_tuple)