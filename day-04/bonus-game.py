import random

answer = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != answer:
    if guess > answer:
        print("Lower")
        guess = int(input("Try again.\n"))
    else:
        print("Higher")
        guess = int(input("Try again.\n"))


print("Congrats, you guessed it!")
