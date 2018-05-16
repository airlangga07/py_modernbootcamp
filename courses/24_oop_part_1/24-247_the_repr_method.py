class User:
    # Class Attributes
    active_users = 0

    # Class Methods
    @classmethod
    def display_active_users(cls):
        return "There are {} active users.".format(cls.active_users)

    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # adding 1 everytime User is created
        User.active_users += 1
    
    def __repr__(self):
        return "{} is {}".format(self.first, self.age)

    def logout(self):
        User.active_users -= 1
        return "{} has logged out".format(self.first)
    
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

# Class Attributes
print(User.active_users)
print(user2.logout())
print(User.active_users)

print(User.display_active_users())

tom = User.from_string("Joe,Saldana,45")
print(tom.first)
print(tom.full_name())