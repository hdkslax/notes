import random

print("Welcome!")

game = ["Rock", "Paper", "Scissors", "Dynamite"]

for i in range(5):
    player = input("Player 1 choice? ")

    computer = random.choice(game)

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player 1 wins!")
        elif computer == "paper":
            print("Computer wins!")


