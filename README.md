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
   * The way the game works is very simple and requires minimal controls. The player follows the story until they are given a choice (this might refer to actions they want to take, directions they want to go, etc.). When they make a choice, the story continues and what happens next depends on the choices they just made (e.g., if the player starts the game by going "left", they end up on a different part of the beach, and if the player goes "inland", they find a forest).

     ![choice](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/choice.png)

3. User can lower or improve their chances of winning by deciding to pick up (or not) an object.
   * To add variety and a bit of difficulty, the player can choose whether they want to pick up certain objects they find at certain points of the game. If they pick up everything they encounter, chances are they will be presented with more choices for survival. For example, in one of the scenarios, the player ends up on the top of the hill and spots a plane. If they picked up a flare gun earlier in the game, they can signal the plane and get rescued which leads to a WIN. If they didn't pick the flare gun up, they cannot use it and the plane never comes which results in a GAME OVER. 

     ![flare-gun](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/flare-gun.png) 

4. Win and loss announcements.
   * Every time a player looses or wins a scenario, they are presented with a win or loss announcement.

     ![loss](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/loss.png) 

     ![win](https://github.com/OlgaJ1989/text_adventure/blob/main/Docs/win.png) 

5. Option to restart the game whether the player loses or wins.
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
      - When I typed "stay" into the terminal, the game lead to a Game Over scenario and the play_again() function was called as expected, allowing me to start again. 
      - When I typed "go", function choice_four() was called as expected.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 
   * Conclusion: This function and all its elements work as expected and no bugs appear.

5. Testing choice_four()
   * When this function is called, the player encounters a boar and is presented with a few options of what they can do in order to try to survive the encounter. The amount of choices the player is given depends on whether they have a knife with them or not (knife can be picked up in choice_two()). If they don't have the knife, they will see 2 choices (to run or to fight with their bare hands). However, if the knife is present, option 3 will appear (throw the knife).
      - To test this is true, I have started the game again, making sure to pick up the knife in choice_two(). I have then made the choice to go inland as this would lead me to the boar. Once I encountered the beast, I expected to see 3 choices and I did, meaning the code works properly. 
      - Next, I have restarted again, making sure NOT to pick up the knife in choice_two(). I have then made the choice to go inland as this would lead me to the boar. Once I encountered the beast, I expected to see only 2 choices and I did, meaning the code works properly.
      - After making sure the proper choices appear depending on whether theknife is present or not, I proceeded with testing the 3 survival choices related to the bear.
      - When I chose "1" (fight with bare hands), the game led to a Game Over scenario and the play_again() function was called as expected, allowing me to start again.
      - When I chose "2" (run), function choice_seven() was called as expected.
      - When I chose "3" (throw knife), I obtained pork which will affect later decisions similarly to the knife. After that, function choice_six() was called as planned.
      - Note that the above choices require an input of an integer for which reason there are two differnt errors displaying if input is incorrect.
      - First error notification: when I tried submitting an empty space or a non-integer character, the ValueError option kicked in, informing me of the wrong input and that the correct one has to be a number. This works as expected. 
      - Second error notification: When I tried submitting a number that isn't the required 1, 2 or 3, I received another error message informing me of the wrong input and that the right one can only be 1, 2 or 3. This works as expected.
   * Conclusion: This function and all its elements work as expected and no bugs appear.

6. Testing choice_six()
   * When this function is called, the player encounters a bear and is presented with a few options of what they can do in order to try to survive the encounter (similarly to what happened with the boar encounter). The amount of choices the player is given depends on whether they have (or not) a flare gun or pork with them (pork can be obtained in choice_four(), flare gun can be picked up in choice_eight()). If they don't have either of these items, they will see 2 choices (to run or to fight with their bare hands). However, if the pork OR flare gun is present, option 3 will appear (distract with pork OR scare off with flare gun - it is not possible to have both items at the same time at any point in the game).
      - To test this is true, I have played the game, making sure to pick up the flare gun in choice_eight(). I have then continued with the choices that would lead me to the bear. Once I encountered the beast, I expected to see 3 choices and I did, meaning the code works properly. 
      - Next, I have restarted again, making sure NOT to pick up the flare gun in choice_eight(). I have then made choices that would lead me to the bear. Once I encountered the beast, I expected to see only 2 choices and I did, meaning the code works properly.
      - Then, I have restarted again, making sure to obtain the pork from the fight with the boar (choice_four()). I have then continued with the choices that would lead me to the bear. Once I encountered the beast, I expected to see 3 choices and I did, meaning the code works properly.
      - As before, I have then played again, making sure not to obtain the pork in the boar encounter (choice_four()). I have then made choices that would lead me to the bear. Once I encountered the beast, I expected to see only 2 choices and I did, meaning the code works properly.
      - After making sure the proper choices appear depending on whether the pork / flare gun are present or not, I proceeded with testing the 4 survival choices related to the bear.
      - When I chose "1" (fight with bare hands), the game led to a Game Over scenario and the play_again() function was called as expected, allowing me to start again.
      - When I chose "2" (run), the game lead to a Game Over scenario and the play_again() function was called as expected, allowing me to start again.
      - When I chose "3" (distract with pork), function game_conclusion() was called as expected.
      - When I chose "3" (scare off with flare gun), function game_conclusion() was called as expected.
      - Note that the above choices require an input of an integer for which reason there are two different errors displaying if input is incorrect.
      - First error notification: when I tried submitting an empty space or a non-integer character, the ValueError option kicked in, informing me of the wrong input and that the correct one has to be a number. This works as expected. 
      - Second error notification: When I tried submitting a number that isn't the required 1, 2 or 3, I received another error message informing me of the wrong input and that the right one can only be 1, 2 or 3. This works as expected.
   * Conclusion: This function and all its elements work as expected and no bugs appear. 

7. Testing choice_seven()
   * In this function, the player is asked whether they would like to go downstream or upstream ("Which direction do you go? (upstream/downstream)).
      - When I typed "upstream" into the terminal, the game continued correctly and the choice_six() function was called as expected.
      - When I typed "donwstream" into the terminal, the game continued correctly and the mushrooms() function was called as expected.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.
   * Conclusion: This function and all its elements work as expected and no bugs appear.  

8. Testing mushrooms()
   * In this function, the user is asked whether they would like to eat mushrooms they found on the beach ("What do you do? (eat/ignore)").
     - When I typed "eat" into the terminal, the game led to a Game Over scenario and the play_again() function was called as expected, allowing me to start again.
     - When I typed "eat" into the terminal, the game led to a Win scenario and the play_again() function was called as expected, allowing me to start again.
     - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.
   * Conclusion: This function and all its elements work as expected and no bugs appear.

9. Testing choice_eight()
   * In this function, the user is asked whether they would like to pick up a flare gun they find in the cockpit ("Do you take it with you? (yes/no)").  
      - When I typed "yes", the game moved to the next part of the story within the same function, as expected. Function choice_six() was called.
      - When I typed "no", the game moved to the next part of the story within the same function, as expected. Function choice_six() was called.
      - When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 
   * Conclusion: This function and all its elements work as expected and no bugs appear. 

10. Testing game_conclusion()
    * Unlike others, this is not a 'choice' function - it simply prints two different endings to the story. 
       - If a player had the chance to pick up the flare gun at any point in the game, the game automatically displays a Win scenario where the flare gun is used to signal the plane leading to a rescue. When I played the game making sure to pick up the flare gun when prompted, I reached the game_conclusion() stage and a Win scenario was triggered, as expected.
       - If no flare gun is present, the game automatically displays a Game Over scenario where the plane doesn't spot them, and they commit suicide in desperation. When I played the game making sure NOT to pick up the flare gun when prompted, I reeached the game_conclusion() stage and a Game Over scenario was triggered, as expected.     
    * Conclusion: This function and all its elements work as expected and no bugs appear.


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

The code is custom and written entirely by me and the story is of my own idea.