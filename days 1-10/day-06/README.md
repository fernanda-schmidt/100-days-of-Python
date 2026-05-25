# 🎯 Day 06: Reeborg's World (Functions & Logic)

## 📌 Description
Instead of a local script, today’s challenge involved navigating "Reeborg's World"—a browser-based game designed to master Python functions, `while` loops, and complex conditional logic.

## 🚀 Features
- **Custom Functions:** Defined `turn_right()` `and jump()` to give the robot new capabilities not found in the base library.
- **Autonomous Navigation:** Implemented logic allowing the robot to solve randomized hurdles and mazes without manual intervention.
- **Edge Case Handling:** Developed algorithms to prevent the robot from getting stuck in infinite loops or crashing into walls.

## 🧠 What I Learned
- **Defining Functions:** How to use the `def`keyword to bundle code into reusable blocks.
- **While Loops:** Using `while not at_goal():` to repeat actions until a specific state is achieved.
- **Indentation and Scope:** Mastering the visual structure of Python, especially when nestling `if`statements inside `while`loops.
 - **Dry Coding (Don't Repeat Yourself):** Using functions to eliminate repetitive code and make the program more readable.

## ▶️ How to Run
The logic for this day was executed on https://reeborg.ca/. No local installation required.

## 🎬 Demo
**Challenge: The Maze** - Logic used to solve the final puzzle:
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

```