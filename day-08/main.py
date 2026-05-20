def greet(name):
    print(f"Hello, {name}!")
    print("Nice to meet you.")


def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left.")

def goodbye():
    print("Well, this has been pleasent.")
    print(f"Bye, {name}, enjoy your life.")

name = input("Enter a name: ").title()
greet(name)

age = int(input("Enter your current age: "))
life_in_weeks(age)

goodbye()




