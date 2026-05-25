# Day 10:  Simple Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        return "ERROR: Cannot divide by 0."
    return a/b


def exponential(a, b):
    return a**b


def modulo(a, b):
    return a % b


print("================================")
print("Welcome to the Python Calculator")
print("================================")

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': exponential,
    '%': modulo,
}


def calculate():
    should_continue = True
    num1 = float(input("Enter the first number: "))

    while should_continue:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("ERROR: Invalid input")
            continue
        num2 = float(input("Enter the next number: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation.\nType "q" to quit.\n').lower()

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_continue = False
            calculate()
        elif choice == 'q':
            should_continue = False
        else:
            print("ERROR: Invalid input")


calculate()
