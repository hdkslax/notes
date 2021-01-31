import random

print("Welcome to Gussing Number!")

randNum = random.randint(1,100)
score = 0

# player 2 can try 3 times
for i in range(3):
    # Ask the player to enter a number in 1~100
    guess = int(input("Please enter a number in 1~100: "))

    # Check if they match and tell them if they won!
    if guess == randNum:
        print("You've got it!")
        # Add to their score
        score = score + 1
    elif guess < randNum:
        print("smaller")
    else:
        print("larger")


# At the end, print out their score
print("You got " + str(score) + "!")
