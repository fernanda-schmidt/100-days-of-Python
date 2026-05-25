# Day 07: Hangman
import random

lives = 7

possibleWords = ['stare', 'cloud', 'pinky', 'spout', 'gamer', 'dusty',
                 'mouse', 'state', 'poser', 'audio', 'adieu', 'miner', 'loser', 'ahead', 'arose', 'ankle', 'bacon', 'beret', 'maker','loath', 'mover', 'clock', 'alone', 'aroma', 'belle', 'basil', 'blame', 'cadet', 'cease', 'camel', 'cargo', 'charm', 'count', 'dough', 'easel', 'elope', 'faith', 'fizzy', 'fluff']

word = random.choice(possibleWords)

display = []
for letter in word:
    display.append("_")  # creates display as list with "_"

while lives > 0 and "_" in display:
    print(f"Remaining lives: {lives}\n")
    print(" ".join(display))  # shows current progress as string, not list
    # gets user guess as lowercase letter
    guess = input("\nGuess a letter: ").lower()
    letterFound = False  # tracks found guesses anywhere in the word

    for i in range(len(word)):
        letter = word[i]
        if guess == word[i]:
            display[i] = guess  # swaps "_" for the letter guessed
            letterFound = True  # checks if letter is found so it doesn't take away a life

    if not letterFound:
        print(f"\n ❌ Try Again\n")
        lives -= 1

if lives == 0:
    print("Game over! You lost!")
    print(f"The word to guess was: {word}")
else:
    print(word)
    print("---------------------------")
    print("\n🥳 Congratulations! You win!")

