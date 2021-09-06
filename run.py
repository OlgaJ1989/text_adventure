import sys
import time


def display_intro():
    """
    Displays game intro
    """
    print()
    print("That was meant to be a holiday of your lifetime.")
    print("Everything went well at first... ")
    print()
    time.sleep(3)
    print("...until the turbulence started...")
    print()
    time.sleep(2)
    print("...followed by darkness...")
    time.sleep(2)
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
    time.sleep(2)
    print("You look around the cabin.")
    print("You seem to be the only one that survived.")
    print()
    time.sleep(3)
    print("You're on your own...")
    print()
    time.sleep(2)
    print("Through one of the remaining windows, you can see that")
    print("you are on what seems like a deserted island.")
    print()
    time.sleep(3)


def start_game():
    """
    Starts the game, asking the user whether they want to get off the island
    or not. If not, game ends. If yes, game continues. If incorrect
    input provided, user is asked the question again.
    """
    while True:
        print("Would you like to try to find a way")
        leave_island = input("to leave the island? (yes/no): ")
        print()
        if leave_island == "no":
            print("Well, it was nice knowing you...")
            time.sleep(2)
            print("Enjoy a slow and painful death from dehydration...")
            print()
            time.sleep(3)
            print("THE END")
            print()
            break
        elif leave_island == "yes":
            get_username()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            print()
            continue


def get_username():
    """
    Continues with the story, asks user to input a name.
    If no input, user asked again. If input provided, game continues.
    Asks user for their first decision.
    """
    print("Great! You made a life-changing decision!")
    time.sleep(2)
    print("However, the world spins when you try to get up...")
    time.sleep(2)
    print("You might have a concusion as the details of the crash are blurry.")
    time.sleep(2)
    print()
    while True:
        name = input("Do you remember who you are? (type name): ")
        if name == "":
            print()
            print("Wrong input. Please provide a name.")
            continue
        else:
            print()
            print(f"Hello, {name}!")
            break
    print()
    print("The tide is coming in, you should get a move on!")
    time.sleep(2)
    print("You can go left along the shore, right along the shore,")
    time.sleep(2)
    print("or inland towards higher ground.")
    print()
    while True:
        choice_one = input("Which way will you go? (left/right/inland): ")
        if choice_one == "right":
            choice_two()
            break
        elif choice_one == "left":
            choice_eight()
            break
        elif choice_one == "inland":
            choice_four()
            break
        else:
            print()
            print("Wrong input. Please type 'left', 'right' or 'inland'.")
            continue


# go right
def choice_two():
    """
    User finds a knife and is asked whether they would like to
    take it or not. The story proceeds either way and the user is asked
    to choose direction again.
    """
    print("You walk until you spot more wreckage from your plane.")
    time.sleep(2)
    print("You decide to search it.")
    time.sleep(2)
    print("You find a knife!")
    time.sleep(2)
    print()
    while True:
        global knife
        knife = input("Do you take it? (yes/no): ")
        if knife == "yes":
            print()
            print("Good choice! That might come in handy!")
            break
        elif knife == "no":
            print()
            print("Well, let's hope you will not live to regret it!")
            break
        else:
            print()
            print("Wrong input. Please type 'yes' or 'no'.")
            continue
    print()
    time.sleep(2)
    print("You continue searching the wreckage until it gets dark.")
    time.sleep(2)
    print()
    while True:
        choice_three = input("Do you stay or go inland? (stay/go): ")
        if choice_three == "stay":
            print("You fell asleep and didn't realise the tide came in.")
            time.sleep(2)
            print("You were swept away to see with the rest of the wreckage")
            time.sleep(2)
            print("and drowned....")
            print()
            time.sleep(3)
            print("GAME OVER")
            break
        elif choice_three == "go":
            choice_four()
            break
        else:
            print()
            print("Wrong input. Please choose to 'go' or 'stay'.")
            continue


# go inland
def choice_four():
    """
    Runs every time user decides to go inland.
    """
    print("You walk inland toward higher ground.")
    time.sleep(2)
    print("The landscape changes and you walk into a dense forest.")
    time.sleep(2)
    print("The darkness is overwhelming...")
    time.sleep(2)
    print("You hear movement in the thicket...")
    time.sleep(2)
    print("You turn around and see...")
    time.sleep(3)
    print()
    boar_string = "A BOAR!!!"
    for character in boar_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(2)
    print()
    print("The beast charges at you! What do you do?!")
    time.sleep(2)
    print()
    print("1. Throw your knife at it!")
    print("2. Fight it with your bare hands!")
    print("3. Run for your life!")
    print()
    choice_five = input("What do you do? (1/2/3): ")
    print()
    while True:
        if choice_five == "1":
            choice_six()
            break
        elif choice_five == "2":
            print("You put up a fight but you're no match for a boar...")
            time.sleep(2)
            print("The boar gored you and you bled out within minutes...")
            print()
            time.sleep(3)
            print("THE END")
            break
        elif choice_five == "3":
            choice_seven()
            break
        else:
            print("Wrong input. Please choose option 1, 2 or 3.")
            continue
        

display_intro()
start_game()
