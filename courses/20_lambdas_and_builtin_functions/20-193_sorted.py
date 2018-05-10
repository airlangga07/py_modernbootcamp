# sorted returns a new sorted list from the items in iterable

more_numbers = [5, 2, 6, 1]
sorted(more_numbers) # 1, 2, 5, 6 it makes a copy of that list
print(more_numbers) # 5, 2, 6, 1

# change the direction of sorted
sorted(more_numbers, reverse=True) # 6, 5, 2, 1

# more powerful way using sorted
users = [
    {"username": "samuel", "tweets": ["i love cake", "i love you"] },
    {"username": "katie", "tweets": ["i love my cat" ] },
    {"username": "jeff", "tweets": [], "color": "purple" },
    {"username": "bob123", "tweets": [] },
    {"username": "doggo_luvr", "tweets": ["dogs are the best"] },
    {"username": "guitar_gal", "tweets": [] }
]

# sort by username by passing in an anonymous function (lambda)
print(sorted(users, key=lambda user: user['username']))
