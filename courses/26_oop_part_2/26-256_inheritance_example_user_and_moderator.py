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

class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1
    
    @classmethod
    def display_active_mods(cls):
        return "There are currently {} active mods.".format(cls.total_mods)
    
    def remove_post(self):
        return "{} removed a post from {}".format(self.full_name(), self.community)


u1 = User("Tom", "Garcia", 35)
jasmine = Moderator("Jasmine", "Oconnor", 61, "Piano")
jasmine2 = Moderator("Jasmine", "Oconnor", 61, "Piano")
print(User.display_active_users())
print(Moderator.display_active_mods())
print(jasmine.full_name())
print(jasmine.community)