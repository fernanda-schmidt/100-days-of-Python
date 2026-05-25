import random

lettersLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!', '@', '#', '$', '%', '&', '*']

print("Let's generate a safe password!")

totalLower = int(
    input("How many lower case letters should your password have?\n"))
totalUpper = int(
    input("How many upper case letters should your password have?\n"))
totalNums = int(input("How many numbers should your password have?\n"))
totalChars = int(
    input("How many special characters should your password have?\n"))

password = []

for i in range(0, totalLower):
    password += random.choice(lettersLower)
for i in range(0, totalUpper):
    password += random.choice(lettersUpper)
for i in range(0, totalNums):
    password += random.choice(nums)
for i in range(0, totalChars):
    password += random.choice(chars)

random.shuffle(password)

finalPassword = ''
for i in password:
    finalPassword += i
    
print(f'Your randomly generated password is: {finalPassword}')

