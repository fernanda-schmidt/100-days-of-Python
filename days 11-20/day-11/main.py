import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    '''Returns a random card form the deck'''
    card = random.choice(cards)
    return card


def calculate_score(cards_dealt):
    '''Calculates the score. Sums the cards_dealt to compare the total to 21.'''
    if sum(cards_dealt) == 21 and len(cards_dealt) == 2:
        return 0

    if (sum(cards_dealt) > 21) and (11 in cards_dealt):
        cards_dealt.remove(11)
        cards_dealt.append(1)

    return sum(cards_dealt)


def compare(user_score, comp_score):
    if user_score == 0 and comp_score == 0:
        return "You both got blackjack! It's a draw!"
    elif user_score == 0:
        return "You win with blackjack!"
    elif comp_score == 0:
        return "The computer wins with blackjack!"
    elif user_score > 21:
        return f"Your cards add up to {user_score}. That's a bust!"
    elif comp_score > 21:
        return "The computer went over 21. You win!"
    elif user_score > comp_score:
        return "You win!"
    elif comp_score > user_score:
        return "The computer wins."
    else:
        return "It's a draw."


def game():
    user = []
    computer = []

    game_over = False

    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        user_score = calculate_score(user)
        print(f"\nYour cards are: {user}. Your current score is: {user_score}")
        comp_score = calculate_score(computer)
        print(f"The computer's first card is: {computer[0]}")

        print()
        if user_score > 21:
            game_over = True
        elif user_score == 0:
            print("==Blackjack!==")
            game_over = True
        else:
            to_continue = input(
                "Enter 'y' to get another card. Type 'n' to pass: ").lower()

            if to_continue == 'y':
                user.append(deal_card())
                computer.append(deal_card())
            elif to_continue == 'n':
                print('You choose to stand.')
                game_over = True
            else:
                print('ERROR: Invalid input.')
                continue
        print()
        if user_score <= 21 and user_score != 0:
            while comp_score < 17 and comp_score != 0:
                computer.append(deal_card())

                comp_score = calculate_score(computer)

    user_score = calculate_score(user)
    comp_score = calculate_score(computer)

    print(compare(user_score, comp_score))
    print(f"\nYour final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {comp_score}")


def play_again():
    again = input(
        "\nWould you like to once more? Enter 'YES' or 'NO': ").lower()
    if again == 'yes':
        game()
    elif again == 'no':
        print("Thanks for playing!")
    else:
        print("ERROR: Invalid Input")


print("===================")
print("Welcome! Let's play")
print("\nBLACKJACK\n")
print("===================")

game()

play_again()

print("===================")
print("\nBLACKJACK\n")
print("===================")
