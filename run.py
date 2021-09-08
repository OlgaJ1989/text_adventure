import sys
import time


global knife
knife = "no"
global pork
pork = False
global flare_gun
flare_gun = "no"


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
            print("GAME OVER")
            print()
            play_again()
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
            print()
            play_again()
            break
        elif choice_three == "go":
            choice_four()
            break
        else:
            print()
            print("Wrong input. Please choose to 'go' or 'stay'.")
            continue


# go inland - boar
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
    print("1. Fight it with your bare hands!")
    print("2. Run for your life!")
    if knife == "yes":
        print("3. Throw your knife at it!")
    print()
    if knife == "yes":
        boar_text = "(1/2/3)"
    else:
        boar_text = "(1/2)"
    while True:
        choice_five = input(f"What do you do? {boar_text}")
        print()
        if choice_five == "3" and knife == "yes":
            continue_without_choice()
            break
        elif choice_five == "1":
            print("You put up a fight but you're no match for a boar...")
            time.sleep(2)
            print("The boar gored you and you bled out within minutes...")
            print()
            time.sleep(3)
            print("GAME OVER")
            play_again()
            break
        elif choice_five == "2":
            choice_seven()
            break
        else:
            print(f"Wrong input. Please choose option {boar_text}")
            continue


def continue_without_choice():
    print("Good aim! You caught the boar right between the eyes!")
    time.sleep(2)
    print("You have pork!")
    global pork
    pork = True
    print()
    choice_six()


def choice_six():
    print("You carry on towards higher ground until you reach an outcrop.")
    time.sleep(2)
    print("You see a cave and decide to inspect it.")
    time.sleep(2)
    print("Wrong idea... You disturb...")
    time.sleep(3)
    print()
    bear_string = "A BEAR!!!"
    for character in bear_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(2)
    print()
    print("Oh no! Think fast! What are your options?")
    print()
    print("1. Fight the bear...")
    print("2. Run for your life!")
    if pork is True:
        print("3. Distract the bear with pork.")
    elif flare_gun == "yes":
        print("3. Scare it off with a flare gun.")
    print()
    time.sleep(2)
    while True:
        bear_choice = input("Which option do you choose? ")
        if bear_choice == "1":
            print("Nice try but you're no match for the bear. ")
            time.sleep(2)
            print("You die...")
            print()
            time.sleep(3)
            print("GAME OVER")
            play_again()
            break
        elif bear_choice == "2":
            print("You run as fast as you can but you can't outrun the bear.")
            time.sleep(2)
            print("It catches up with you and mauls you to death...")
            time.sleep(3)
            print()
            print("GAME OVER")
            play_again()
            break
        elif bear_choice == "3" and pork is True:
            print("You distract the bear with pork and manage to run away.")
            time.sleep(2)
            print()
            choice_nine()
            break
        elif bear_choice == "3" and flare_gun == "yes":
            print("You scare the bear off with the flare gun!")
            time.sleep(2)
            print()
            choice_nine()
            break
        else:
            print("Wrong input. Please choose ")


def choice_seven():
    print()
    print("You run as fast as you can and eventually loose the boar.")
    time.sleep(2)
    print("When you stop to catch your breath, you hear flowing water.")
    time.sleep(2)
    print("You found a stream.")
    time.sleep(2)
    print("You can follow it upstream or downstream.")
    time.sleep(2)
    while True:
        stream = input("Which direction do you go? (upstream/downstream): ")
        if stream == "upstream":
            choice_six()
            break
        elif stream == "downstream":
            print("You eventually end up on the beach")
            time.sleep(2)
            print("with plenty of rocks and branches lying.")
            time.sleep(2)
            print("You make a sign big enough for passing planes to see.")
            time.sleep(2)
            print("All you can do now is wait...")
            time.sleep(3)
            mushrooms()
            break
        else:
            print("Wrong input. Please type 'downstream' or 'upstream'.")
            continue


def mushrooms():
    print("You spot some mushrooms at the edge of the beach.")
    time.sleep(2)
    print("You know they might be poisonous but you're really hungry.")
    time.sleep(2)
    while True:
        shrooms = input("What do you do? (eat/ignore): ")
        if shrooms == "eat":
            print("The plane arrives only to find your dead body.")
            time.sleep(2)
            print("The mushrooms were poisonous after all...")
            time.sleep(3)
            print()
            print("GAME OVER")
            print()
            play_again()
            break
        elif shrooms == "ignore":
            print("You ignore the mushrooms and take a sip of water")
            print("from the stream instead.")
            time.sleep(2)
            print("Water keeps you alive long enough for the plane")
            print("to spot and rescue you.")
            time.sleep(2)
            print("Well done! YOU WON!!!")
            time.sleep(3)
            print()
            play_again()
            break
        else:
            print("Wrong input. Please type 'eat' or 'ignore'.")


def choice_eight():
    print("You walk towards the setting sun.")
    time.sleep(2)
    print("Eventually you find the plane's cockpit.")
    time.sleep(2)
    print("Inside you find a flare gun.")
    time.sleep(2)
    while True:
        global flare_gun
        flare_gun = input("Do you take it with you? (yes/no): ")
        if flare_gun == "yes":
            print()
            print("Good choice! That might come in handy!")
            break
        elif flare_gun == "no":
            print()
            print("Well, let's hope you will not live to regret it!")
            break
        else:
            print()
            print("Wrong input. Please type 'yes' or 'no'.")
            continue
    print()
    time.sleep(2)
    print("Past the wreckage, a river flows into the ocean.")
    time.sleep(2)
    print()
    choice_six()


def choice_nine():
    print("After escaping the bear, you walk until you reach the hill top.")
    time.sleep(2)
    print("Suddenly, you see a plane in the sky!")
    time.sleep(2)
    print()
    if flare_gun == "yes":
        print("You take aim and fire the flare gun to alert the plane.")
        time.sleep(2)
        print("The plane grows smaller and eventually fades from view...")
        print()
        time.sleep(3)
        print("...but not for long...")
        print()
        time.sleep(3)
        print("After spotting your signal, the plane comes back.")
        time.sleep(2)
        print("You get rescued!!!")
        print()
        time.sleep(3)
        print("Well done! YOU WON!")
        print()
        play_again()
    else:
        print("You wave frantically but the crew doesn't see you.")
        time.sleep(2)
        print("You watch the plane get smaller and fade from view...")
        time.sleep(2)
        print("You are filled with despair...")
        time.sleep(2)
        print("Unwilling to accept your fate, you jump into a ravine")
        print()
        time.sleep(3)
        print("GAME OVER")
        print()
        play_again()


def play_again():
    while True:
        play_again = input("Would you like to play again? (yes/no)")
        if play_again == "yes":
            global knife
            knife = "no"
            global pork
            pork = False
            global flare_gun
            flare_gun = "no"
            start_game()
            break
        elif play_again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


display_intro()
start_game()
