# example
msg = input("what is the secret password? ")

while msg != "bananas":
    print("WRONG! ")
    msg = input("what is the secret password? ")

print("CORRECT!")

# another example
for num in range(1, 11):
    print(num)

# we can do that with while
num = 1
while num < 11:
    print(num)
    num += 1
