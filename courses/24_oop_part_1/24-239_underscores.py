class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like turtles!"
        self.__lol = "HAHAH"

p = Person()

print(p.name)
print(p._secret)
# print(p.__msg)
print(dir(p))
print(p._Person__lol)