file = open('story.txt')
file.read()

# go to position
file.seek(0)
file.read()

# get the lines
file.readline()

# gives all the lines and preseves them in a list
file.readlines()

# file close
file.close()