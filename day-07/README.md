# 🎯 Day 07: Hangman

## 📌 Description
A fully functional command-line Hangman game where the player attempts to guess a randomly selected 5-letter word one letter at a time before running out of lives.

## 🚀 Features
- **Dynamic Progress Tracking:** Uses list manipulation to dynamically reveal correctly guessed letters while hiding the rest behind underscores `(_)`.
- **Delayed Penalty Logic:** Implements a tracking flag `(letterFound)` to ensure a player only loses a life after the program evaluates the entire word.
- **Dynamic Loop Control:** Utilizes Python's `in` operator `(while "_" in display)` to instantly trigger a win state the moment all letters are revealed.

## 🧠 What I Learned
- **Lists vs. Strings:** Learned why tracking changing characters is vastly more efficient inside a mutable list than an immutable string.
- **Index-Based Iteration:** Using `range(len(word))` to find and replace items at precise index positions within a list.
- **State Flagging:** Implementing boolean trackers to control conditional execution after a loop finishes running.
- **String Joining:** Using the `' '.join()` method to cleanly present a collection of list elements as a readable string to the player.

## 🎬 Demo
![Program Demo](./hangman.gif)

## ▶️ How to Run
```bash
python main.py
```

