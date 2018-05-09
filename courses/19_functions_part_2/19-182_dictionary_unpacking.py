def display_names(first, second):
    print("{} says hello to {}".format(first, second))

names = { "first": "Charlie", "second": "sue" }

display_names(**names)
