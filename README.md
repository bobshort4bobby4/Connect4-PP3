
computer_move_scored()

get array of valid columns
get array of first available row positions ifor each valid column
for each valid column drop apiece into first row position using tempboard
            send this temp board to be scored for each position returning a score for that column to be stored in an scored array
            take highest score from scored array and return as best column for computer to drop piece



How to score ???
re- use winning position code

set score to zero
use .count  method to count x and o in each batch of 4 add to score or not for each batch
when all position scored return score to be stored in scored array

looks suspiciously simple!





























computer_![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome bobshort4bobby4,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!