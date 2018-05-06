instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "My Favorite Number!"
}

print(instructor.values())

# iterate through values
for v in instructor.values():
    print(v)

# iterate through keys
for k in instructor.keys():
    print(k)

# accessing values and keys 
for key, value in instructor.items():
    print('{} - {}'.format(key, value))
