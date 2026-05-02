# Day 2 Challenge:
# Tip Calculator
# Get the user's input for Subtotal, Tip, and how many people are splitting.
# Create a "Tip Calculator" from those inputs

print("=============================")
print("Welcome to the Tip Calculator")
print("=============================")

bill = float(input("What was the bill total?\n"))
tip = (int(input("How much would you like to tip? 20 | 25 | 30\n"))) / 100
people = int(input("How many people are splitting the bill?\n"))

tip = bill*tip
total = bill + tip
totalEach = total / people

print(
    f"With a bill of\n${bill:.2f}\nAnd a total tip of\n${tip:.2f}\nEach person should pay\n${totalEach:.2f}\n")
