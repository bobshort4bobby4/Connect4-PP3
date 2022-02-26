
# **Connect4**

(CTRL + Click to open links in new window)

The deployed site can be found [here](https://minipproject.herokuapp.com/)

Github repository can be accessed [here](https://github.com/bobshort4bobby4/Connect4-PP3)   
  
    
![a mockup of the deployed application](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/mockup-pp3.png)
  
    
      
      
# **Introduction**
  
This my third project undertaken as part of the [Code Institute Full Stack Diploma Course](https://codeinstitute.net)  
   
It is a version of the classic board game **Connect4**, implmented using the Python coding language and deployed via heroku to the web.  

It was designed by Wexler and Strongin and **NOT** as I believed for many years by [David Bowie](https://en.wikipedia.org/wiki/David_Bowie) which is an urban myth.  

The game was first sold in 1974 by MB games of Springfield MA.  It was a global success and spawned many spin-offs and variations.
  
The rules are simple, each player has 21 checkers of the same colour, either red or yellow in the original game.  The players take turns placing their checkers into a 6 by 7 
grid, the grid is suspended vertically and the pieces drop to the first available position.  

The winner is the first player to connect a line of four of their particular colour.  

If neither player connects a line of four before the grid is full then the game is a draw.  

More information regarding the game can be found at this link. [Connect4 Wikipedia Page is here](https://en.wikipedia.org/wiki/Connect_Four)  



  
# User Experience/User Interface (UX/UI)

<details>  
            
<summary>User Experience/User Interface (UX/UI)</summary>  
  
  ### User Stories
  
  ##### First Time Visitor Goals
  As a first time visitor I want: 
  - the rules and final aim of the game to be obvious so that I can use the site easily.  
  - to be entertained and engaged with the game from the initial load so I will have a positive experience using the site.  
  - the game to function correctly and gameplay to be intuitive so that I do not have any frustrating emotions using the site.  
  - to be able to play the game on various different devices so that I can play when convenient.
  - to have any incorrect input rejected and the error explained clearly and quickly so I do not have any frustrating emotions using the site. 
   
  ##### Return/frequent Visitor Goals.
  As a return/frequent visitor I want:  
  - to be able to gauge my performance so that I can track my skill level .
  - to be able to increase difficulty of the game so that I can challenge myself.
  - to be able to play the game on various different devices so that I can access the site when convenient.
            
  ##### Website's Owner Goals.
  As the developer I want:
  - to provide a fun game so I feel I have produced a quality website.
  - to provide a game to stimulate mental function so that I provide a worthwhile experience for the user.
  - to encourage continued use of the game so that the site is a success.
  
  ### FlowCharts
  
  A Flowchart for the python script in shown below as well as a link to the pdf of same.  
    
  
  [Link to Flowchart Pdf can be found here](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/Flow-pp3.pdf)    
  
  ![screenshot of flowchart](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/Flow-pp3.png) 
  
    
  ### WireFrames
  
  The design is very basic and does not change, consequently I felt a one page Wireframe would be sufficent showing the basic lay-out of the site.
    
  A [link to the pdf file for the Wireframes is here.](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/wireframe-pp3.pdf)  
   
  
  ![image of desttop and mobile wireframes](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/wireframe-pp3.png)
  
  ### Background Image
  
  In order to add visual appeal I used a repeating tile as a background image.  It is a picture of a section of the gameboard.  
  
  [Link to background tile](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRv1hN01fHPr6M-NnNxNb7mD1u5nlTCVo1F7A&usqp=CAU)  
    
    
  ![the background image tile](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/connect-tile-pp3.jpg)
  
 
</details>

  
  # Features
    
  <details>
     <summary>Features</summary>
  
  
  ### Welcome Screen
  On loading the initial screen displays a title in ascii art and some background information about the game. Brief play instructions are also included. 
  The game pauses on this screen untill the user hits the return key.
    
  ![a screen shot of the welcome screen](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/welcomescreen-pp3.png)
    
  ### Level Screen
  When the User presses the return key, the level screen is displayed.  
  This screen shows the 3 possible difficulty levels the user may choose.   
  This setting governs how the computer moves are picked.  
  The User is required to pick one from the three options of Easy, Medium or Hard.  
    
  ![a screenshot of the levelscreen](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/difflevelinput-pp3.png)  
    
 After the User picks a level the screen shows which player is to go first (randomly choosen by program), then pauses before clearing and displaying the initial board.
  
  ### Game Screen  
  The game screen consists of the board display and a prompt to the User to pick a move.   
  The computer moves happen instantly after each User move.  
    
  ![a screen shot of the initial game screen](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/initialscreen-pp3.png)  
    
    
  ### Game Over
  The players take turns until the game is won or drawn.  
  A message is displayed stating if a win or draw, which player won and how many moves were taken by them.  
  The User is asked to input either quit or play again.  
  If the User opts to exit the finish screen is displayed and the program exits,  
  alternatively the program loops back to the welcome screen and a new game is initiated.
    
  ![a screenshot of the game over screen](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/gamewon-pp3.png)  
    
    
  ### Finish Screen
  If the User opts to quit a message is displayed and the program finishes.  
    
  ![a screen shot of the finish message](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/finishscreen-pp3.png)  
    
  ### Future Features
  At some point as time resources allow I would like to implement the MiniMax algorithm for the hard level.
  This is a recursive algorith used to determine optimal moves.  
  It creates a tree for each possible gameboard and backtracks through each to score each board.  
  
  It would improve the visual aspect of the program if the two types of pieces were coloured differently  
  and highlighted in a third colour when a line of four was made. 
  </details>

# Technologies Used
<details>
  <summary>Technologies Used</summary>
  
  #### Languages Used
  
  - Python
  - CSS  
  
  #### Python Libraries
  
  [random](https://docs.python.org/3/library/random.html) was used to generate a random integer
  used in the computer_move_random method of the Player Class and to determine which player should
  take first turn in the display_intro method of the Board Class.
  
  [copy](https://docs.python.org/3/library/copy.html?highlight=copy#module-copy) deepcopy() used to copy board state
  into temp_board in computer_move_scored() method of the Player Class.  
    
  [time](https://docs.python.org/3/library/time.html?highlight=time#module-time) used to pause game in the init_game()
  method of the Player Class.  
    
  [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) used to create ASCII art text in
  display_intro() method of Board Class and play_again() method of Board Class.  
    
    
  
  #### Applications Used
  
  - [Balsamiq](https://www.balsamiq.com) was used to create wireframes for this project.
  - [LucidChart](https://www.lucidchart.com) used for the flowchart in readme file.
  - [Git](https://git-scm.com/) Git was used for version control.
  - [GitHub](https://github.com/) GitHub is used to store the projects code.
  - [Heroku](http://www.heroku.com/) Heroku.com was used to deploy the site.
  - [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) used for layout and responsive testing.
  - [Wave](https://wave.webaim.org/) used for accessibility testing.
  - [favICO.com](https://convertico.com/favicon/) used for creating favicon.
  - [W3 Validator](https://jigsaw.w3.org/css-validator/) used to test css code.
  - [pep8online](http://pep8online.com/) pep8online used to validate python code
  - [WAVE](https://wave.webaim.org/) used to check for accessibility.
  - [Windows snip & sketch](https://www.microsoft.com/en-us/p/snip-sketch/9mz95kl8mr0l?activetab=pivot:overviewtab) used to capture screenshots for readme file.
  - [techsini.com](https://techsini.com/) used to create the mock-up used in the readme file.
  
 </details>
  
# Testing


<details>

  <summary>Testing</summary>
  
  
### WAVE Accessibilty Tool
  The deployed version was tested using this site. The first test produced one contrast error, caused by the red colour of the 'Run Program' button not contrasting well with the background image I had choosen.  
I changed the button colour to blue. This adjusted site produced no errors, result is shown below.  
    
  ![a screen shot of the WAVE test result](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/waveresult-pp3.png)  
    
### CSS Validation  
  I made minimal changes to the css integral to  the template provided, namely changes to the positioning of the terminal, adding a background image and changing the colour of the 'Run Program' to blue.  I tested the `body` and `button` css fragments using the w3c validator and no errors or warning were generated.
   
   
### PeP8 Linter
  I submitted all python files to pep8online.com and cleared all errors and warnings.  
  Screen shots of the results can be found [here](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/pep8linter.md)
  
### LightHouse Testing
  The Lighthouse testing tool built in to the Chrome browser was used on the deployed web-site. A screen shot of the result is shown below.  
  
  ![a screen shot of the lighthouse testing result](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/lighthouseresult-pp3.png)
  
  
### Manual Validation of User Input
  I manually tested all aspects of user input and the results are linked below.
  
  
  
[Link to User input testing data](https://docs.google.com/spreadsheets/d/15SZgouY_8Q-GX0ia4hHf1ua2u9JLxhJGwFfNRMPtTl4/edit?usp=sharing)
  
### Testing of Win Check and Scoring Algorithms
  In order to ensure the win check and scoring aspects of the program were functioning correctly. I inserted a nested for loop in the relevant scripts, which placed consecutive numbers in the array, the code and the resulting array is shown below.  
  
  ![a screen shot of nested loops used to fill array with test data](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/nestloopfortest-pp3.png)
    
    
  ![a screen shot of resulting array](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/testingarray-pp3.png)
  
  I then put a print command in the scripts which output each slice to be assessed to the terminal.  I was then able to run the program in debug mode and manually check that the correct slices were being generated at each iteration of the scoring/check win function.  
  An example of these terminal outputs is shown below.  
  
  ![a screen shot of output slices](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/diagstest-pp3.png)  
    
  I found several mistakes either in index assignment or in code blocks wrongly indented which were causing errors using this method.  
  An example is shown below where the column loop was working incorrectly causing only the first column to be scored, this was an indentation error.
  
  ![a screen shot of a bug found](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/scoringtesting%20bug%20found-pp3.png)  
    
    
  ### Testing game for achievement of User Goals.  
  
  
  |                       Goal                                              |                          Outcome                                                               |
  |-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
  |The rules and final aim of the game to be obvious                        |Instructions displayed on welcome screen.                                                       |
  |To be entertained and engaged with the game from the initial load.       |Colour used in an effort to engage user.                                                        |
  |The game to function correctly and gameplay to be intuitive.             |No logic errors in code, actions to be taken intuitive.                                         |
  |To be able to play the game at different difficulty levels.              |Three levels provided.                                                                          |
  |To have any incorrect input rejected and the error explained clearly.    |All User input validated and appropriate messages output to User.                               |     |To be able to gauge/score my performance.                                |Moves taken is shown to the player.                                                             |     |To be able to play the game on different devices.                        |Game works on range of devices.                                                                 |
  |To provide a fun game.                                                   |Game provides a reasonable challenge and is easy to use.                                        |
  |To provide a game to stimulate mental function.                          |Game play requires attention and focus.                                                         |
  |To encourage continued use of the game.                                  |Colour used in an effort to entertain user and encourage continued use.                         |
   
    
  ### Issues
  If the deployed game is left unattended for any period of time, it freezes and will not take input. The browser needs to be refreshed or the 'Run Program' button clicked to start a new game.  This is not an issue on a locally run version of the game. I do not know why this is happening.  
    
If the human player is drawn to take first turn it is still quite easy to win the game. Because the computer always scores the board using the same method it is possible to build up an knowledge as to where the piece will be placed. After repeated games it is possible to learn ways of winning every time.  
    
    
  ### Video Screen Capture Of Deployed Heroku APP.
    
    
  

https://user-images.githubusercontent.com/77545206/155849867-20b45e68-27da-4be8-a268-18b0f3384693.mp4


  
</details>
  
# Deployment

<details>
  
  <summary>Heroku</summary>  
  
### Heroku

Heroku is a cloud based platform that allows the user to deploy and manage apps easily.  Heroku is fully managed meaning that all the hardware/server issues are taken care of.
It allows the linking of github repositories which makes deploying easier.

To deploy my project I followed the steps below.

1. Goto the [Heroku home page](https://www.heroku.com/) and open an account.
1. Goto your dashboard and click on the 'new ' button in the top right of the screen.  
  ![screenshot of new button](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/heroku-newapp-pp3.png)  
1. From the drop down list choose 'Create new App'.
  ![a screen shot of the create new app page in heroku](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/createnewapp-heroku-pp3.png)  
  
  
1. Choose a name for your project and the region you are in. Click 'Create App'
1. Click on the 'Settings' tab.
  ![a screen shot of the settings tab](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/settingheroku-ppp3.png)  
1. Click 'Reveal Config Vars.
1. Enter `port` and `8000` as a key:value pair and press `Add`  
1. Click 'add buildpack'
1. Add the Python buildpack then the nodejs one. Click 'Save'  
  ![a screen shot of the buildpack screen](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/buildpack-pp3.png)
1. Select the 'Deploy' tab.
1. Choose the'Connect to GitHub' option from the 'Deployment Method' section.
  ![a screen shot of the github deployment section](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/settingtab-herku-pp3.png)

1. Search for and enter the 'repo-name' in the input area.
  
  ![a screen shot of the repo name input area](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/reponame-pp3.png)  
1. Click 'Connect'.
1. Choose either `Enable Automatic Deploys` or `Deploy Branch'.  I chose the former.
1. The site should now be deployed.  Click the 'Overview' tab and the 'Latest activity' should ahve a 'build succeeded' message diplayed.
   The deployment log can be also accessed on the github repository under the 'Environments' section to the right of the page.
  
![a screen shot of the buid succeeded](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/buildsucceeded-pp3.png)
  
[The site is now live](https://minipproject.herokuapp.com/)
  
![a picture of the deployed site](https://github.com/bobshort4bobby4/Connect4-PP3/blob/main/assets/images/readme-screenshots/deployedheroku-pp3.png)


</details>

  
  # Credits
  
  <details>
  
  <summary>Credits</summary>
  
  In order to learn how computers play against human opponents I used many resources on the internet, chief amongst these were [Wikipedia](https://en.wikipedia.org/wiki/Category:Game_artificial_intelligence) and [Keith Galli's github](https://github.com/KeithGalli?tab=repositories).   
  
  
  Huge thanks to my CI Mentor Mr. Benjamin Kavanagh.
</details>

 # Note on Difficulty Options  
 
 <details>
  <summary>Difficulty Levels</summary>
  
The computer moves are calculated in different ways for each of the levels.    
  
The first (easy level) is completely random, a random number is picked in the column range and provided that column has remaining space, the piece is dropped there.  
  
The medium and hard levels use a simple scoring scheme which gives every position on the board a score based on that particular moves value to the computer player.  
The piece is dropped in the column with the highest score.  
All possible positions are scored on the hard level, some of the diagonal line slices are not scored on the medium level, thereby creating a "blind spot" for the computer.  
  
This method of scoring is by no means perfect but offers a reasonable challenge to the casual player.  
  
Details of how I implemented this scoring scheme are given below, I should say that the general method I learned from various resources on the internet but the implementation is my own.  I choose to place an token (in my case '*' into the temporary board for scoring which I did not see any other implementation use (others placed their player piece), this allowed me to be more specific in the scoring process.  As to the merits or disadvantages of this way of doing it I have not tested.

###### Easy Level
  
  This method picks a column for the computer player on easy difficulty level.
  
  If the choosen column not full:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pick a random column number in range zero to six  
      return that column number  
  
    
###### Medium Level
  
  These are the steps I used to pick a column for the computer player on medium difficulty level.
    
  **computer_move_scored() Method of Player Class**  
  
  Determine opposing player piece type, store in op_piece.  
  Determine columns which are not full, store in an array valid_cols, with a -1 entry if column full.  
  Determine first available position in each column, store in an array first_available_row.  
  For each valid column in valid_cols:  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make a deepcopy of state of the playing board named temp_board.  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Place a '*' into the lowest empty position of that column.  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send temp_board to player.scoring_function method.  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Append returned score to final_scores array.  
  Determine index of highest score in final_scores array, store in variable col.  
  Return col.    
    
    

 **player.scoring_function Method of Player Class** 
    
  Create score variable  
  For each row in temp_board:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create an array for each row called row_array  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each row_array:  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Slice into sections of four positions, stored in array called slice4.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send each slice4 to player.scoring_logic.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add returned value to score.  
    
  For each column in temp_board:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create an array for each column called column_array  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each column_array:  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Slice into sections of four positions, stored in array called slice4.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send each slice4 to player.scoring_logic.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add returned value to score.    
    
  For each forward-leaning diagonal column (left-hand side) in temp_board:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create an array for each section called diagfor_array  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each diagfor_array:  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Slice into sections of four positions, stored in array called slice4.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send each slice4 to player.scoring_logic.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add returned value to score.    
    
  For each backward-leaning diagonal column(right-hand side) in temp_board:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create an array for each row called diagback_array  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each diagback_array:  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Slice into sections of four positions, stored in array called slice4.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send each slice4 to player.scoring_logic.  
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add returned value to score.  
  Return score  
    
    
 **player.scoring_logic Method of Player Class** 
    
  Create score variable.  
  Add value to score for each slice4 on the following basis.  
  If slice4 contains:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 player pieces and 1  asterisk  add 2000  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 player pieces and 1  asterisk add 1000  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 player piece and 3 empty add 100  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is column 3 add 50.  
  
  If slice4 contains:  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 op_piece and 1 asterisk add 10000  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 op_piece and 1 empty add 2000  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 op_piece add 1500  
    
  If slice4 contains op-pieces in the middle indexes and an asterisk at either index[0] or index[3] add 7000.  
  Return score  
    
  
  
  ###### Hard Level
  
  The steps are the same as the medium level except all diagonal columns are scored.

</details>
  

















































