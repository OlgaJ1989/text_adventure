# STRANDED. A text-based adventure game.

![Gameplay](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/gameplay.gif)

STRANDED is a Python terminal game inspired by classic text-based adventure games such as Zork. It runs in the Code Institute mock terminal on Heroku.

The player's goal is to survive and get off a deserted island that they are stranded on after a plane crash. The player's survival depends on the decisions they make during the game.

The game is not aimed at any type of audience in particular but might be especially fun to older players who used to play the original text-based adventure games back in the seventies.  

The live version of my project can be accessed [here](https://stranded.herokuapp.com/).

## How to play

When the program is first run, the player is presented with the intro to the story and then asked whether they would like to play ("Would you like to find a way to leave the island?"). If the asnwer is "yes", the player is asked to provide a username and the game continues from there. 

The way the game works is very simple and requires minimal controls. The player follows the story until they are given a choice (this might refer to actions they want to take, directions they want to go, etc. ). When they make a choice, the story continues and what happens next depends on the choices they just made (e.g. if the player starts the game by going "left", they end up on a different part of the beach, and if the player goes "inland", they find a forest).

To add variety and a bit of difficulty, the player can also choose whether they want to pick up certain objects they find at certain points of the game. Even if they think they made the right decision, their survival might depend on whether they previously decided to pick up an encountered object or not.

The player wins when they manage to take all the right decisionsneeded to be rescued from the island. If they fail, they will be asked whther they would like to try again. 

## Game Logic Flowchart

![Flowchart](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/flowchart.png)

## Technologies

* Python was used as the programming language to make the game.
* [LucidChart](https://www.lucidchart.com/pages/) was used to create the flow chart showing the game's logic.
* [GitHub](https://github.com/) has been used to store the code, images, and other content. 
* [Heroku](https://dashboard.heroku.com/apps) was used to deploy the game to the web.
* [Git](https://git-scm.com/) was used to track changes made to the project and to commit and push code to the repository.
* Python module [time](https://docs.python.org/3/library/time.html) has been used to allow for a delay between lines of text displaying. 
* Python module [sys](https://docs.python.org/3/library/sys.html) has been used to print a string of text character by character instead of all at one.  

## Testing

### Validator testing

No errors were found when code passed through the [PEP8](http://pep8online.com/checkresult) linter.

![PEP8](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/linter.png)

### Bugs / Other

I manually tested the whole gameplay playing through every scenario, especially focusing on the below:
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