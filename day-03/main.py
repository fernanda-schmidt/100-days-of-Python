# Day 03 Challenge:
# Choose Your Own Adventure
# Use if/elif/else statements to create a game where the user's input changes the outcome.

print("====================")
print("Welcome to the Game!")
print("====================")
print("Let's play.")
print("====================")
print()
print("You stand before the Obsidian Temple. The massive stone doors are open.\nTo the left is a narrow tunnel smelling of damp earth.\nTo the right, a grand staircase leading into the darkness.")

leftRight = input("Do you turn\n\tLEFT or RIGHT?\n").upper()

if (leftRight == "LEFT"):
    print("You find a subterranean stream.")
    swimOrBridge = input(
        "Do you swim across or look for a bridge?\n\tSWIM or BRIDGE\n").upper()
    if (swimOrBridge == "SWIM"):
        print("Oh no! There were crocodiles in the water!")
        print("GAME OVER")
    elif (swimOrBridge == "BRIDGE"):
        print('You\'ve encountered the Temple Guardian.')
        riddleOrRun = input(
            "Do you: answer his riddle or try to run?\n\tRIDDLE or RUN\n").upper()
        if (riddleOrRun == "RUN"):
            print("You fool! You can't run from the Temple Guardian!")
            print("GAME OVER")
        elif (riddleOrRun == "RIDDLE"):
            print("The Temple Guardian gave you a riddle and you answered correctly!")
            print("The Temple Guardian steps aside, revealing three chests: gold, silver and lead. Which do you choose?")
            chestChoice = input("\tGOLD or SILVER or LEAD\n").upper()
            if (chestChoice == "GOLD"):
                print(
                    "It was a decoy! The gold disappears just as you try to grab it.\n\tYOU LOSE")
            elif (chestChoice == "SILVER"):
                print("Oh no! The chest was filled with cursed dust!\n\tYOU LOSE")
            elif (chestChoice == "LEAD"):
                print("CONGRATULATIONS!\nYou have found the True Treasure!\n\tYOU WIN!")
            else:
                print("ERROR: You wandered by yourself and entered an unknown command")
                print("GAME OVER")
        else:
            print("ERROR: You wandered by yourself and entered an unknown command")
            print("GAME OVER")
    else:
        print("ERROR: You wandered by yourself and entered an unknown command")
        print("GAME OVER")
elif (leftRight == "RIGHT"):
    print("You entered a hall full of statues. Do you walk through the center of them or crawl along the shadows?")
    walkCrawl = input("\tWALK or CRAWL").upper()
    if (walkCrawl == "WALK"):
        print("A trap door triggers! Spears fly from the walls and hit you.")
        print("GAME OVER")
    elif (walkCrawl == "CRAWL"):
        print("You safely reach the end of the hall, where you find the Temple Guardian")
        print("The Temple Guardian gave you a riddle and you answered correctly!")
        print("The Temple Guardian steps aside, revealing three chests: gold, silver and lead. Which do you choose?")
        chestChoice = input("\tGOLD or SILVER or LEAD\n").upper()
        if (chestChoice == "GOLD"):
            print(
                "It was a decoy! The gold disappears just as you try to grab it.\n\tYOU LOSE")
        elif (chestChoice == "SILVER"):
            print("Oh no! The chest was filled with cursed dust!\n\tYOU LOSE")
        elif (chestChoice == "LEAD"):
            print("CONGRATULATIONS!\nYou have found the True Treasure!\n\tYOU WIN!")
        else:
            print("ERROR: You wandered by yourself and entered an unknown command")
            print("GAME OVER")
    else:
        print("ERROR: You wander into a trap by giving an unknown command.")
        print("GAME OVER")
else:
    print("You chose an unkown command and the temple collapsed.\nGAME OVER")
