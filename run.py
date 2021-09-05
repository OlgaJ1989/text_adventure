import sys
import time


def displayIntro():
    """
    Display game intro
    """
    print()
    print("That was meant to be a holiday of your lifetime.")
    print("Everything went well at first... ")
    print()
    time.sleep(3)
    print("...until the turbulence started...")
    print()
    time.sleep(3)
    print("...followed by darkness...")
    time.sleep(3)
    print()
    print("You wake up after what feels like hours,")
    print("only to realise your plane crashed and you are...")
    print()
    print()
    time.sleep(4)
    print("     ##############################")
    print("     #                            #")
    print("     #          STRANDED          #")
    print("     #                            #")
    print("     ##############################")
    print()
    print()
    time.sleep(3)


def startGame():
    """
    Starts the game
    """
    while True:
        leaveIsland = input("Try to find a way off the island?: (yes/no) ")
        print()
        if leaveIsland == "no":
            print()
            print("Well, it was nice knowing you...")
            print("Enjoy a slow and painful death from dehydration...")
            print()
            print("THE END")
            break
        elif leaveIsland == "yes":
            getUsername()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            print()
            continue


def getUsername():
    name = input("Great! Do you remember who you are? (type name) ")


displayIntro()
startGame()
