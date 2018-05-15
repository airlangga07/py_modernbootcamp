class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def initials(self):
        return "{}.{}".format(self.first[0], self.last[0])
    
    def likes(self, likes):
        return "{} likes {}".format(self.first, likes)
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return "Happy Birthday {}".format(self.first)

user1 = User("Jose", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)

print(user1.full_name())
print(user2.full_name())

print(user1.likes("Candy"))
print(user2.likes("Ice Cream"))

print(user1.initials())
print(user2.initials())

print(user1.is_senior())
print(user2.is_senior())

print(user1.birthday())
print(user2.birthday())