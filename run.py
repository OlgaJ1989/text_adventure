import sys
import time


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
    leaveIsland = input("Do you want to find a way off the island?: (yes/no) ")
    if leaveIsland == "no":
        print()
        print("Well, it was nice knowing you...")
        print("Enjoy a slow and painful death from dehydration.")
    elif leaveIsland == "yes":
        print()
        name = input("Great! Do you remember who you are? (type name) ")
    else:
        print()
        print("Wrong input. Please type 'yes' or 'no'.")


startGame()
