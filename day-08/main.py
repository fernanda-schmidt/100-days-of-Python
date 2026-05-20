# Day 08 - The Ceasar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

programRunning = True


def caeserCipher(message, shift):
    encryptedString = ""

    for letter in message:
        if letter in alphabet:
            letterIndex = alphabet.index(letter)
            newIndex = (letterIndex + shift) % len(alphabet)
            encryptedString += alphabet[newIndex]
        else:
            encryptedString += letter

    print(encryptedString)


while programRunning:
    userInput = input(
        "Enter a message to encrypt or decrypt. Type 'quit' to quit.\n")
    if userInput == 'quit':
        programRunning = False
        break

    shift = int(input("How much is the shift?\n"))

    choice = input(
        "Enter 'encode' to encrypt. Type 'decode' to decrypt. Type 'quit' to quit.\n").lower()

    if choice == 'encode':
        caeserCipher(userInput, shift)
    elif choice == 'decode':
        caeserCipher(userInput, (-shift))
    elif choice == 'quit':
        programRunning = False
    else:
        print("ERROR: Invalid input.")

print("Thanks for using the Caeser Cipher Decryptor.")
