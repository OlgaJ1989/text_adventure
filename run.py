import sys
import time


# Global variables
global knife
knife = "no"
global pork
pork = False
global flare_gun
flare_gun = "no"


def display_intro():
    """
    Displays game intro and title
    """
    print()
    print("That was meant to be a holiday of your lifetime.")
    print("Everything went well at first...\n ")
    time.sleep(3)
    print("...until the turbulence started...\n")
    time.sleep(2)
    print("...followed by darkness...\n")
    time.sleep(2)
    print("You wake up after what feels like hours,\n" +
          "only to realise your plane crashed and you are...\n\n")
    time.sleep(4)
    print("     ##############################")
    print("     #                            #")
    print("     #          STRANDED          #")
    print("     #                            #")
    print("     ##############################\n\n")
    time.sleep(2)
    print("You look around the cabin.")
    time.sleep(2)
    print("You seem to be the only one that survived.\n")
    time.sleep(3)
    print("You're on your own...\n")
    time.sleep(2)
    print("Through one of the remaining windows, you can see that\n" +
          "you are on what seems like a deserted island.\n")
    time.sleep(3)
    start_game()


def start_game():
    """
    Starts the game, asking the user whether they want to get off the island
    or not. If not, game ends. If yes, game continues to get_username function.
    If incorrect input provided, user is asked the question again.
    """
    while True:
        leave_island = input("Would you like to try to find a way " +
                             "to leave the island? (yes/no):\n")
        if leave_island == "no":
            print("\nWell, it was nice knowing you...")
            time.sleep(2)
            print("Enjoy a slow and painful death from dehydration...\n")
            time.sleep(3)
            print("GAME OVER\n")
            play_again()
            break
        elif leave_island == "yes":
            get_username()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


def get_username():
    """
    Continues with the story, asks user to input a name. If no input,
    user asked again. If input provided, game continues giving the user
    three directions to choose from: right (choice_two function), left
    (choice_eight function), inland (choice_four function). If incorrect input
    provided, user is asked the question again.
    """
    print("\nGreat! You made a life-changing decision!")
    time.sleep(2)
    print("However, the world spins when you try to get up...")
    time.sleep(2)
    print("You might have a concusion as details of the crash are blurry.\n")
    time.sleep(2)
    while True:
        name = input("Do you remember who you are? (type name):\n")
        if name == "":
            print("Wrong input. Please provide a name.")
            continue
        else:
            print(f"Hello, {name}!")
            break
    print("\nThe tide is coming in, you should get a move on!")
    time.sleep(2)
    print("You can go left along the shore, right along the shore,\n" +
          "or inland towards higher ground.\n")
    while True:
        choice_one = input("Which way will you go? (left/right/inland):\n")
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
            print("Wrong input. Please type 'left', 'right' or 'inland'.")
            continue


# go right / knife
def choice_two():
    """
    Asks the user whether they would like to pick up a knife they found.
    Whether the user picks it up or not, the story proceeds the same way and
    the user is asked to choose again. Choice 'stay' means GAME OVER.
    Choice 'go' leads to choice_four function (inland). If incorrect input
    provided, user is asked the question again.
    """
    print("\nYou walk until you spot more wreckage from your plane.")
    time.sleep(2)
    print("You decide to search it.")
    time.sleep(2)
    print("You find a knife!\n")
    time.sleep(2)
    while True:
        global knife
        knife = input("Do you take it? (yes/no):\n")
        if knife == "yes":
            print("\nGood choice! That might come in handy!")
            break
        elif knife == "no":
            print("\nWell, let's hope you will not live to regret it!")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue
    time.sleep(2)
    print("You continue searching the wreckage until it gets dark.\n")
    time.sleep(2)
    while True:
        choice_three = input("Do you stay or go inland? (stay/go):\n")
        if choice_three == "stay":
            print("\nYou fell asleep and didn't realise the tide came in.")
            time.sleep(2)
            print("You were swept away to see with the rest of the\n " +
                  "wreckage and drowned....\n")
            time.sleep(3)
            print("GAME OVER\n")
            play_again()
            break
        elif choice_three == "go":
            choice_four()
            break
        else:
            print("Wrong input. Please choose to 'go' or 'stay'.")
            continue


# go inland / boar
def choice_four():
    """
    Runs every time user decides to go inland. User encounters a boar and is
    given a choice of what to do to survive. Option 1 leads to GAME OVER,
    option 2 leads to choice_seven function (stream) and continues with the
    story. Option 3 appears only if user decided to pick up the knife earlier
    (as it suggests throwing it at the bear) and leads to choice_six function.
    If incorrect input provided, user is asked the question again.
    """
    print("\nYou walk inland toward higher ground.")
    time.sleep(2)
    print("The landscape changes and you walk into a dense forest.")
    time.sleep(2)
    print("The darkness is overwhelming...")
    time.sleep(2)
    print("You hear movement in the thicket...")
    time.sleep(2)
    print("You turn around and see...\n")
    time.sleep(3)
    boar_string = "A BOAR!!!\n"
    for character in boar_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(2)
    print("\nThe beast charges at you! What do you do?!\n")
    time.sleep(2)
    print("1. Fight it with your bare hands!")
    print("2. Run for your life!")
    if knife == "yes":
        print("3. Throw your knife at it!")
    if knife == "yes":
        boar_text = "(1, 2 or 3)"
    else:
        boar_text = "(1 or 2)"
    while True:
        try:
            choice_five = int(input(f"What do you do? {boar_text}:"))
            if choice_five == 3 and knife == "yes":
                print("\nGood aim! You caught it right between the eyes!")
                time.sleep(2)
                print("You skin the boar and you have pork now!")
                global pork
                pork = True
                choice_six()
                break
            elif choice_five == 1:
                print("\nYou put up a fight but you're no match for a boar...")
                time.sleep(2)
                print("The boar gores you and you bleed out\n" +
                      "within minutes...\n")
                time.sleep(3)
                print("GAME OVER\n")
                play_again()
                break
            elif choice_five == 2:
                choice_seven()
                break
            else:
                print(f"Wrong number. Please type {boar_text}.")
                continue
        except ValueError:
            print(f"Wrong input. Please type in a number {boar_text}.")
            continue


# bear
def choice_six():
    """
    User encounters a bear and is given a choice of what to do to survive.
    Options 1 and 2 lead to GAME OVER. There are two versions of option 3.
    One appears only if user has pork and the other appears only if user has
    a flare gun. Both version of option 3 lead to choice_nine function. If
    incorrect input provided, user is asked the question again.
    """
    print("\nYou carry on towards higher ground until you reach an outcrop.")
    time.sleep(2)
    print("You see a cave and decide to inspect it.")
    time.sleep(2)
    print("Wrong idea... You disturb...\n")
    time.sleep(3)
    bear_string = "A BEAR!!!\n"
    for character in bear_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(2)
    print("\nOh no! Think fast! What are your options?\n")
    print("1. Fight the bear...")
    print("2. Run for your life!")
    if pork is True:
        print("3. Distract the bear with pork.")
    elif flare_gun == "yes":
        print("3. Scare it off with a flare gun.")
    time.sleep(2)
    if pork is True or flare_gun == "yes":
        bear_text = "(1, 2 or 3)"
    else:
        bear_text = "(1 or 2)"
    while True:
        try:
            bear_choice = int(input(f"Which do you choose? {bear_text}:"))
            if bear_choice == 1:
                print("\nNice try but you're no match for the bear. ")
                time.sleep(2)
                print("It mauls you and you die from your injuries...\n")
                time.sleep(3)
                print("GAME OVER\n")
                play_again()
                break
            elif bear_choice == 2:
                print("\nYou run as fast as you can but you can't outrun it!")
                time.sleep(2)
                print("It catches up with you and mauls you to death...\n")
                time.sleep(3)
                print("GAME OVER\n")
                play_again()
                break
            elif bear_choice == 3 and pork is True:
                print("\nYou distract the bear with pork and run away.")
                time.sleep(2)
                game_conclusion()
                break
            elif bear_choice == 3 and flare_gun == "yes":
                print("\nYou scare the bear off with the flare gun!")
                time.sleep(2)
                game_conclusion()
                break
            else:
                print(f"Wrong input. Please choose {bear_text}.")
                continue
        except ValueError:
            print(f"Wrong input. Please type in a number {bear_text}.")
            continue


# stream
def choice_seven():
    """
    User asked whether they want to go downstream or upstream. 'Upstream'
    leads to choice_six function and 'downstream' leads to mushrooms function.
    If incorrect input provided, user is asked the question again.
    """
    print("\nYou run as fast as you can and eventually loose the boar.")
    time.sleep(2)
    print("When you stop to catch your breath, you hear flowing water.")
    time.sleep(2)
    print("You found a stream.")
    time.sleep(2)
    print("You can follow it upstream or downstream.\n")
    time.sleep(2)
    while True:
        stream = input("Which direction do you go? (upstream/downstream):\n")
        if stream == "upstream":
            choice_six()
            break
        elif stream == "downstream":
            print("\nYou eventually end up on the beach\n" +
                  "with plenty of rocks and branches lying around.")
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


# mushrooms
def mushrooms():
    """
    Asks user to make a decision about eating mushrooms. 'Eat' leads to GAME
    OVER. 'Ignore' leads to a WIN. If incorrect input provided, user is asked
    the question again.
    """
    print("\nYou spot some mushrooms at the edge of the beach.")
    time.sleep(2)
    print("You know they might be poisonous but you're really hungry...")
    time.sleep(2)
    while True:
        shrooms = input("\nWhat do you do? (eat/ignore):\n")
        if shrooms == "eat":
            print("\nThe plane arrives only to find your dead body.")
            time.sleep(2)
            print("The mushrooms were poisonous after all...\n")
            time.sleep(3)
            print("GAME OVER\n")
            play_again()
            break
        elif shrooms == "ignore":
            print("\nYou ignore the mushrooms and take a sip of water\n" +
                  "from the stream instead.")
            time.sleep(2)
            print("Water keeps you alive long enough for the plane\n" +
                  "to spot and rescue you.\n")
            time.sleep(2)
            print("Well done! YOU WON!!!\n")
            time.sleep(3)
            play_again()
            break
        else:
            print("Wrong input. Please type 'eat' or 'ignore'.")


# go left / flare gun
def choice_eight():
    """
    Asks user whether they want to pick up a flare gun. Both choices lead to
    choice_six function. If wrong input provided, user asked again.
    """
    print("\nYou walk towards the setting sun.")
    time.sleep(2)
    print("Eventually you find the plane's cockpit.")
    time.sleep(2)
    print("Inside you find a flare gun.\n")
    time.sleep(2)
    while True:
        global flare_gun
        flare_gun = input("Do you take it with you? (yes/no):\n")
        if flare_gun == "yes":
            print("\nGood choice! That might come in handy!")
            break
        elif flare_gun == "no":
            print("\nWell... Let's hope you won't live to regret it!")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue
    time.sleep(2)
    print("Past the wreckage, a river flows into the ocean.")
    time.sleep(2)
    choice_six()


# hill top
def game_conclusion():
    """
    Checks if user picked up the flare gun. If yes, user wins. If no, GAME
    OVER.
    """
    print("\nAfter escaping the bear, you walk until you reach the hill top.")
    time.sleep(2)
    print("Suddenly, you see a plane in the sky!")
    time.sleep(2)
    if flare_gun == "yes":
        print("You take aim and fire the flare gun to alert the plane.")
        time.sleep(2)
        print("The plane grows smaller and eventually fades from view...\n")
        time.sleep(3)
        print("...but not for long...\n")
        time.sleep(3)
        print("After spotting your signal, the plane comes back\n " +
              "and you get rescued!\n")
        time.sleep(3)
        print("Well done! YOU WON!\n")
        play_again()
    else:
        print("You wave frantically but the crew doesn't see you.")
        time.sleep(2)
        print("You watch the plane get smaller and fade from view...")
        time.sleep(2)
        print("You are filled with despair...")
        time.sleep(2)
        print("Unwilling to accept your fate,\n" +
              "you jump into a ravine and die...\n")
        time.sleep(3)
        print("GAME OVER\n")
        play_again()


# restart game
def play_again():
    """
    Called every time a game is lost or won. Asks user whether they would like
    to play again. If not, goodbye message is displayed. If Yes, play_game
    function is called again.
    """
    while True:
        play_again = input("Would you like to try again? (yes/no):\n")
        if play_again == "yes":
            global knife
            knife = "no"
            global pork
            pork = False
            global flare_gun
            flare_gun = "no"
            display_intro()
            break
        elif play_again == "no":
            print("\nThat's a shame... Thanks for playing!\n")
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


display_intro()
