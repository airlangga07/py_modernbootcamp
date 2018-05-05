import random

random_number = random.randint(1, 10)
guess = 0

while guess !== random_number:
    guess = int(input("Pick a number from 1 to 10: "))

    if guess > random_number:
        print("Too high...")
    elif guess < random_number:
        print("Too low...")
    else:
        print("YOU WON!")

print(random_number)
