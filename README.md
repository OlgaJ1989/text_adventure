# STRANDED. A text-based adventure game.

![Gameplay](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/gameplay.gif)

STRANDED is a Python terminal game inspired by classic text-based adventure games such as Zork. It runs in the Code Institute mock terminal on Heroku.

The player's goal is to survive and get off a deserted island that they are stranded on after a plane crash. The player's survival depends on the decisions they make during the game.

The game is not aimed at any type of audience in particular but might be especially fun to older players who used to play the original text-based adventure games back in the seventies.  

The live version of my project can be accessed [here](https://stranded.herokuapp.com/).


## How to play

The game is very easy to play as it requires minimal controls. All the player has to do is type in required words when prompted by the terminal.

The player's goal is to survive and get off a deserted island that they are stranded on after a plane crash. The player's survival depends on the decisions they make during the game. 

When the game first loads, the player is presented with a story and asked whether they would like to play. If the answer is yes, the player can then customise the story by inputting their name. From that point on, the story continues, providing the player with choices such as which direction they would like to go next, whether they would like to pick up an item they found, or if they would like to fight any of the encountered wild animals. What the player sees next depends on the choices they've just made so they need to think carefully about every choice in order to survive and win.


## Features  

1. The opportunity to customise the game with user's own name.
   * When the program is first run, the player is presented with the intro to the story and then asked whether they would like to play ("Would you like to find a way to leave the island?"). If the answer is "yes", the player is asked to provide a username and the game continues from there.

     ![name](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/name.png)

2. User has the power over where the story goes as the plot changes based on the choices the user makes.
   * The way the game works is very simple and requires minimal controls. The player follows the story until they are given a choice (this might refer to actions they want to take, directions they want to go, etc.). When they make a choice, the story continues and what happens next depends on the choices they just made (e.g. if the player starts the game by going "left", they end up on a different part of the beach, and if the player goes "inland", they find a forest).

     ![choice](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/choice.png)

3. User can lower or improve their chances of winning by deciding to pick up (or not) an object.
   * To add variety and a bit of difficulty, the player can choose whether they want to pick up certain objects they find at certain points of the game. If they pick up everything they encounter, chances are they will be presented with more choices for survival. For example, in one of the scenarios, the player ends up on the top of the hill and spots a plane. If they picked up a flare gun earlier in the game, they can signal the plane and get rescued which leads to a WIN. If they didn't pick the flare gun up, they cannot use it and the plane never comes which results in a GAME OVER. 

     ![flare-gun](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/flare-gun.png) 

4. Win and loss announcements.
   * Every time a player looses or wins a scenario, they are presented with a win or loss announcement.

     ![loss](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/loss.png) 

     ![win](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/win.png) 

5. Option to restart the game whether the player looses or wins.
   * No matter what the outcome for the player is, they will be able to restart the game and explore different scenarios.

     ![play-again](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/play-again.png)
    

## Technologies

* Python was used as the programming language to make the game.
* [LucidChart](https://www.lucidchart.com/pages/) was used to create the flow chart showing the game's logic.
* [GitHub](https://github.com/) has been used to store the code, images, and other content. 
* [Heroku](https://dashboard.heroku.com/apps) was used to deploy the game to the web.
* [Git](https://git-scm.com/) was used to track changes made to the project and to commit and push code to the repository.
* Python module [time](https://docs.python.org/3/library/time.html) has been used to allow for a delay between lines of text displaying. 
* Python module [sys](https://docs.python.org/3/library/sys.html) has been used to print a string of text character by character instead of all at one.  
* [Xbox Game Bar](https://www.microsoft.com/en-us/p/xbox-game-bar/9nzkpstsnw4p?activetab=pivot:overviewtab) was used to records the screen and [ezgif.com](https://ezgif.com/video-to-gif) was used to convert a part of it to a gif for the Readme file intro.


## Testing

### Validator testing

No errors were found when code passed through the [PEP8](http://pep8online.com/checkresult) linter.

![PEP8](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/linter.png)

### Bugs / Other

I manually tested the whole gameplay playing through every scenario, using the below flowchart for reference:

![Flowchart](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/flowchart.png)

#### Steps:

1. Testing game_intro()
   * I have started my testing with the game_intro() function, making sure it correctly displays the beginning of the story and that time.sleep() delays the printing of following sentences as planned (the default timing has been set to 2 seconds but is changed to 3 in certain parts of the game for dramatic effect). This function and all its elements work as expected and no bugs appear. 

2. Testing start_game() 
   * In this function, player is asked whether they would like to play or not ("Would you like to find a way to leave the island? (yes/no)). 
      - When I inputted "yes" into the terminal, the game continued correctly and the get_username() function was called next as expected.
      - When I inputted "no" into the terminal, the game displayed a Game Over message and the play_again() function was called as expected, allowing me to start again.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.
   * Conclusion: This function and all its elements work as expected and no bugs appear.  

3. Testing get_username()
   * In this function, player is asked to provide a username ("Do you remember who you are? (type name)). They can input anything but a blank input.
      - When I inputted my name or any other word / character, an f-string was correctly printed with the chosen value ("Hello, {value}") and the game then proceeded correctly with the next part of the story.
      - When I tried to submit an empty input by not typing anything in and just pressing Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.
   * After inputting the username, the function continued with the story until I was asked to choose a direction ("Which way will you go? (left/right/inland)).
      - When I chose "left", function choice_eight() was called as expected.  
      - When I chose "right", function choice_two() was called as expected.  
      - When I chose "inland", function choice_four() was called as expected.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.  
   * Conclusion: This function and all its elements work as expected and no bugs appear.

4. Testing choice_two()
   * In this function, the user is asked whether they would like to pick up a knife they find in the wreckage ("Do you take it? (yes/no)").  
      - When I typed "yes", the game moved to the next part of the story within the same function, as expected.
      - When I typed "no", the game moved to the next part of the story within the same function, as expected.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 
   * After the 'knife choice' section, the story continued for a bit until I was asked whether I would like to spend the night in the wreckage or go elsewhere ("Do you stay or go inland? (stay/go)")  
      - When I typed "stay" into the terminal, the game lead to a Game Over scenario the play_again() function was called as expected, allowing me to start again. 
      - When I typed "go", function choice_four() was called as expected.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 
   * Conclusion: This function and all its elements work as expected and no bugs appear.

5. Testing choice_four()






1. I have checked that all functions work as expected and lead to correct outputs / choices. 
2. I have checked that all while loops lead to correct options if user inputs correct option number or display errors if the number is incorrect. I have also made sure that the try/except statement included in two of the while loops displays a ValueError when a number isn't inputted at all.  
3. I have made sure that the user sees correct options displayed depending on whether they possess (or not) an item they had the chance to pick up earlier in the game (knife/flare gun/pork). If a user is missing the required item when fighting the bear or the boar, they should only see 2 options to save themselves. If the user possesses any of the extra items, they will see 3 choice options instead of 2.

No errors or bugs were found when above testing was carried out. All functions, loops and other structures work as expected.  


## Deployment

The below steps were followed to deploy this project to Heroku:
1. Go to [Heroku](https://dashboard.heroku.com/apps) and click "New" to create a new app.
2. After choosing the app name and setting the region, press "Create app".
3. Go to "Settings" and navigate to Config Vars. Add a Config Var with a key word of called PORT and a value of 8000.
4. Still in the "Settings", navigate to Buildpacks and add buildpacks for Python and NodeJS (in order).
5. Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub.
Once GitHub is chosen, find your repository and connect it to Heroku.
6. Scroll down to Manual Deploy, make sure the "main" branch is selected and click "Deploy Branch". 
7. The deployed app can be found [here](https://stranded.herokuapp.com/).


## Credits

The mock terminal used to host the game has been created by Code institute.