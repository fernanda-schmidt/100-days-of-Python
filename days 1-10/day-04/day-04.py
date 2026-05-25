import random

print("Welcome!\nLet's play a game of Rock, Paper, Scissors!")

comp = random.randint(1,3)


user = int(input("Enter 1 for Rock, 2 for Paper and 3 for Scissor.\n"))

match user:
    case 1:
        print("You chose ROCK")
    case 2:
        print("You chose PAPER")
    case 3:
        print("You chose SCISSORS")
    case _:
        print("ERROR: Invalid Input. Try again")
        
match comp:
    case 1:
        print("Computer chose: ROCK")
    case 2:
        print("Computer chose: PAPER")
    case 3:
        print("Computer chose: SCISSORS")

# The Judge Logic
if user == comp:
    print("It's a tie!")
elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 2):
    print("You win! ")
else:
    print("The computer wins! ")

