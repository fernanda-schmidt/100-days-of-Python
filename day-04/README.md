# 🎯 Day 04: Rock, Paper, Scissors

## 📌 Description
A classic hand-game played between the user and the computer. This program utilizes Python's randomization capabilities and logic structures to determine a winner in real-time.

## 🚀 Features
### 1. Rock, Paper, Scissors Game:
- Randomized Opponent: Uses the *RANDOM* module to ensure the computer makes an unpredictable game every time.
- Pattern Matching: Implements Python *MATCH-CASE* syntax for clean user input handling.
- Instant Win/Loss Logic: Automatically evaluates game rules to declare a winner or a tie.

### 2. BONUS: Guessing Game (bonus-game.py)
 - Dynamic Feedback: Tells the player to go "Higher" or "Lower" based on their guess.
 - Persistent Gameplay: Uses a while loop to keep the game running until the correct number is found.
 - Randomized Targets: Generates a new secret number (1–10) every time you play.

## 🧠 What I Learned
 - The Random Module: Generating integers with random.randint().
 - Structural Pattern Matching: Using match and case for clean input handling.
 - Loops: Using while loops to repeat code until a specific condition is met.
 - Conditional Logic: Nesting if/else inside loops to provide real-time user feedback.



## ▶️ How to Run
### To play the main game:
```bash
python main.py
```
NOTE: Because the program uses Match-Case statements, it requires Python 3.10 or higher to run.

### To play the bonus Guessing Game:
``` bash
python bonus-game.py
```

## 🎬 Demo
### Rock Paper Scissors Game:
![Program Demo](./rock-paper-scissors.gif)

### Bonus Guessing Game:
![Program Demo](./bonus-game.gif)
