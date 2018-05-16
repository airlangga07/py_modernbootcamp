class Animal:
    cool = True

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

class Cat(Animal):
    pass

a = Animal()
a.make_sound("CHIRP")

blue = Cat()
blue.make_sound("MEOW")

print(Animal.cool)
print(Cat.cool)
print(blue.cool)

print(isinstance(blue, Cat))
print(isinstance(blue, Animal))