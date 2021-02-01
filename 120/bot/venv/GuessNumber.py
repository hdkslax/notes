import random

print("Welcome to the Guess Number!")

randNum = random.randint(1,100) # 产生1-100之间的随机数，包含1和100
score = 5

for i in range(5):
    print(i)
    guess = int(input("Please enter a numebr in 1~100: "))

    if guess < randNum:
        print("Please enter a larger number.")
        score -= 1
    elif guess > randNum:
        print("Please enter a smaller number.")
        score -= 1
    else:
        break # 强行停止游戏

print("Your score is: " + str(score))