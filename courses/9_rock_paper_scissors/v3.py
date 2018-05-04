import random

print("Rock..")
print("Paper..")
print("Scissors..")

player = input("Player 1, make your move: ").lower()
rand_num = random.randint(0, 2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Computer plays {}".format(computer))

if player == computer:
    print("its a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player 1 wins!")
    elif computer == "paper":
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player 1 wins!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("Player 1 wins!")
    elif computer == "rock":
        print("Computer wins!")
else:
    print("something went wrong...")
