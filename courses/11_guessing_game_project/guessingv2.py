import random

random_number = random.randint(1, 10)
guess = 0

while True:
    guess = int(input("Pick a number from 1 to 10: "))

    if guess > random_number:
        print("Too high...")
    elif guess < random_number:
        print("Too low...")
    else:
        print("YOU WON!")
        play_again = input("Do you want to play again (y/n)? ")
        if (play_again == 'y'):
            random_number = random.randint(1, 10)
            guess = 0
        else:
            print("Thank you for playing!")
            break


print(random_number)
