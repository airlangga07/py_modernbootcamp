# modes for opening files
# r - Read a file (no writing)
# w - write to a file (prev contents removed)
# a - append to a file (prev contents not removed)
# r+ - read and write to a file (writing based on cursor)

# with open('haiku.txt', 'a') as file:
#     file.write("Here is one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Lets go check it out!\n")

# r+
# with open("haiku.txt", "r+") as file:
#     file.write(":)")
#     file.seek(10)
#     file.write(":)")
