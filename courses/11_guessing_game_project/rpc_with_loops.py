import random

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print("Player score: {} Computer score: {}".format(player_wins, computer_wins))

    player = input("Player 1, make your move: ").lower()

    # if the player wants to quit
    if player == "quit" or player == "q":
        break

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
            player_wins += 1
        elif computer == "paper":
            print("Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player 1 wins!")
            player_wins += 1
        elif computer == "scissors":
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player 1 wins!")
            player_wins += 1
        elif computer == "rock":
            print("Computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid code...")

if player_wins > computer_wins:
    print("Congrats you won!")
elif player_wins == computer_wins:
    print("Its a tie.")
else:
    print("Oh no! Computer won!")
