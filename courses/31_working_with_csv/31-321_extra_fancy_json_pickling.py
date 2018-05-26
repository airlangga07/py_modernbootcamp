import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Charles", "Tabby")


# opening a file
with open('cat.json', 'r') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)