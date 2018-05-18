class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name
    
    def swim(self):
        return "{} is swimming".format(self.name)
    
    def greet(self):
        return "I am {} of the sea!".format(self.name)


class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT")
        self.name = name
    
    def walk(self):
        return "{} is walking".format(self.name)

    def greet(self):
        return "I am {} of the land.".format(self.name)


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT")
        super().__init__(name=name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print("captain cook is instance of Penguin: {}".format(isinstance(captain_cook, Penguin)))
print("captain cook is instance of Aquatic: {}".format(isinstance(captain_cook, Aquatic)))
print("captain cook is instance of Ambulatory: {}".format(isinstance(captain_cook, Ambulatory)))