#Day 12: Number Guessing Game
import random

answer = random.randint(1,100)

print(answer) #TODO delete later

def set_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        print(f'You chose: {difficulty}')
        return 10
    elif difficulty == 'hard':
        print(f'You chose: {difficulty}')
        return 5
    else:
        return -1
    
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print("You got it!")
        return True
        

attempts = set_difficulty()

while attempts > 0:
    print(f'You have {attempts} attempts remaining.')
    
    guess = int(input("Guess a number: "))
    if check_answer(guess, answer):
        break
    attempts -=1
    
    if attempts == 0:
        print("You've run out of guesses. You lose.")
        print(f"The answer was {answer}")
