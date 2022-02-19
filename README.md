
# **Connect4**

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

More information regarding the game can be found [here](https://en.wikipedia.org/wiki/Connect_Four)  



  
# User Experience/User Interface (UX/UI)

<details>  
            
<summary>User Experience/User Interface (UX/UI)</summary>  
  
  ### User Stories
  
  ##### First Time Visitor Goals
  As a first time visitor I want: 
  - the rules and final aim of the game to be obvious so that I can use the site easily.  
  - to be entertained and engaged with the game from the initial load so I will have a positive experience using the site.  
  - the game to function correctly and gameplay to be intuitive so that I do not have any frustrating emotions using the site.  
  - to be able to play the game on various different devices so that I can challenge myself at different skill levels.
  - to have any incorrect input rejected and the error explained clearly and quickly so I do not have any frustrating emotions using the site. 
   
  ##### Return/frequent Visitor Goals.
  As a return/frequent visitor I want:  
  - to be able to gauge my performance so that I can track my skill level .
  - to be able to challenge myself by increasing difficulty of the game so that I can challange myself.
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
  
  In order to add visual appeal I useda repeating tile as a background image.  It is a picture of a section of the gameboard.  
  
  [Link to background tile]()  
    
    
  ![the background image tile]()
  
 
</details>


# Deployment

<details>
  
  <summary>Heroku</sumarry>  
  
### Heroku

Heroku is a cloud based platform that allows the user to deploy and manage apps easily.  Heroku is fully managed meaning that all the hardware/server issues are taken care of.
It allows the linking of github repositories which makes deploying easier.

To deploy my project I followed the steps below.

1. Goto the [Heroku home page](https://www.heroku.com/) and open an account.
1. Goto your dashboard and click on the 'new ' button in the top right of the screen.  
                             ![screenshot of new button]()  
1. From the drop down list choose 'Create new App'.
                             ![a screen shot of the create new app page in heroku]()  
  
  
1. Choose a name for your project and the region you are in. Click 'Create App'
1. Click on the 'Settings' tab.
                             ![a screen shot of the settings tab]()  
1. Click 'Reveal Config Vars.
1. Enter `port` and `8000` as a key:value pair and press `Add`  
1. Click 'add buildpack'
  ![a screen shot of the buildpack screen]()
1. Add the Python buildpack then the nodejs one. Click 'Save'
                             ![a screen shot of the buildpack screen]()
  
1. Select the 'Deploy' tab.
1. Choose the'Connect to GitHub' option from the 'Deployment Method' section.
                             ![a screen shot of the github deployment section]()

1. Search for and enter the 'repo-name' in the input area.
  
   ![a screen shot of the repo name input area]()  
1. Click 'Connect'.
1.  Choose either `Enable Automatic Deploys` or `Deploy Branch'.  I chose the former.
1. The site should now be deployed.  Click the 'Overview' tab and the 'Latest activity' should ahve a 'build succeeded' message diplayed.
  The deployment log can be also accessed on the github repository under the 'Environments' section to the right of the page.
  
[**The site is now live](https://minipproject.herokuapp.com/)
  
![a picture of the deployed site]()


</details>
























mockup website  https://techsini.com/




























The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

