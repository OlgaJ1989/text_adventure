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
    time.sleep(2)
    print("You look around the cabin.")
    print("You seem to be the only one that survived.")
    print()
    time.sleep(2)
    print("You're on your own...")
    print()
    time.sleep(2)
    print("Through one of the remaining windows, you can see that")
    print("you are on what seems like a deserted island.")
    print()
    time.sleep(2)


def start_game():
    """
    Starts the game, asking the user whether they want to get off the island
    or not. If not, game ends. If yes, game continues. If incorrect
    input provided, user is asked the question again.
    """
    while True:
        print("Would you like to find a way")
        leave_island = input("to leave the island? (yes/no): ")
        print()
        if leave_island == "no":
            print()
            print("Well, it was nice knowing you...")
            print("Enjoy a slow and painful death from dehydration...")
            print()
            print("THE END")
            print()
            break
        elif leave_island == "yes":
            get_username()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


def get_username():
    """
    Continues with the story, asks user to input a name.
    If no input, user asked again. If input provided, game continues.
    Asks user for their first decision.
    """
    print("Great! You made a life-changing decision!")
    print("However, the world spins when you try to get up...")
    print("You might have a concusion as the details of the crash are blurry.")
    print()
    while True:
        name = input("Do you remember who you are? (type name): ")
        if name == "":
            print("Wrong input. Please provide a name.")
            continue
        else:
            print()
            print(f"Hello, {name}!")
            break
    print()
    print("The tide is coming in, you should get a move on!")
    print("You can go left along the shore, right along the shore,")
    print("or inland towards higher ground.")
    print()
    while True:
        choice_one = input("Which way will you go? (left/righr/inland): ")
        if choice_one == "left":
            choice_two()
            break
        elif choice_one == "right":
            choice_three()
            break
        elif choice_one == "inland":
            choice_four()
            break
        else:
            print()
            print("Wrong input. Please type 'left', 'right' or 'inland'.")
            continue


def choice_two()


def choice_three()


def choice_four()


display_intro()
start_game()
