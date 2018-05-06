instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "My Favorite Number!"
}

# this is possible to check whether if the key exist in a dict
print("name" in instructor) # True
print("phone" in instructor) # False

# to check if the values is exist, we can use .values() 
print(4 in instructor.values()) # True
