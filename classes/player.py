"""
Module containing the Player Class
representing the players of the game

Class: Player
"""


import random
import copy
import time
from classes.ClearMixin import *

class Player(ClearMixin):
    """
    Class representing the players of the game

    Parameters:
    Clearmixin: Mixin Class - clears the terminal screen

    Methods:
    def init_game(): initialises the game

    def computer_move_random (): determines the computer move on easy difficulty setting

    def computer_move_scored(): determines the computer move on medium difficulty setting

    def scoring_function(): breaks the playimg board into chunks of
                            4 positions and passes these to the scoring algorithm

    def scoring_logic(): scores each slice of 4 positions 
    """

    def __init__(self, name, piece):
        """
        Constructs the attributes for the Player object.

        Attributes:
        name: str - the name of that player

        piece: str - the playing piece of that player
        """
        self.name = name
        self.piece = piece
    
    @staticmethod
    def init_game(game):

        """
        Displays introduction screen (via game.display_intro),
        determines play order and displays initial board to screen
        Creates two instances of the Player Class

        Parameters:
        game: an instance of Board Class

        Variables:
        pause: int - used to set time delay in time.sleep command

        level: str - used to store difficulty level
                    (returned from game.display_intro method)

        first: int - randomly generated to determine which player goes first

        player1: an instance of the Player Class

        player2: an instance of the Player Class

        Returns:
        player1: an instance of the Player Class

        player2: an instance of the Player Class

        level: str - stores the difficulty level for the current game
        """
        pause = 2
        level = game.display_intro()
        first = random.randint(1, 2) # decides play order, creates players
        if first == 1:
            player1 = Player("Human", "x")
            player2 = Player("Computer", "0")
            print( "\033[5;31m" + "Human to go first" + '\033[39m')
            time.sleep(pause)
        else:
            player1 = Player("Computer", "x")
            player2 = Player("Human", "0")
            print( "\033[5;31m" + "\033[5m" + " Computer to go first" + '\033[39m' )
            time.sleep(pause)
        
        ClearMixin().clrscr()
        game.draw_board()
        return player1, player2, level


    def computer_move_random (self,board):
        """
        Generates random computer move, used on easy difficulty level

        Parameters:
        board: object  - representing the current playing board

        Variables:
        invalid_col: boolean - used to control while loop
                                 which generates the column choice

        col: int - stores the column choice

        Returns:
        col: int - stores the column choice.
        """

        invalid_col = True
        while invalid_col:
            col = random.randint(0,6)
            if board[0][col] == "_":
                invalid_col = False
        return col


    def computer_move_scored(self, player, board, player1, player2):
        """ 
        Generates computer moves based on a simple position scoring system,
        used on the medium difficulty level

        Parameters:
        player: object - representing the current player

        board: object - representing the current state of the board

        player1: an instance of the Player Class

        player2: an instance of the Player Class

        Variables:
        final_score: array - stores the list of scores for each column

        player.piece: object attritute str - the computer's playing piece type

        op_piece: str - the human's playing piece type

        valid_cols: array - list of columns in which it is valid to place piece

        first_available_row: array - list of positions in which a
                                     played piece would land for each column 

        temp_board: array - a deepcopy of the current playing board

        col: int - stores the choice of column picked to play

        Returns:
        col: int - stores the choice of column picked to play.                           

        returns column choice
        """

        # get opposing piece to implement blocking move scoring
        final_scores = []
        if player.piece == player1.piece:  
            op_piece = player2.piece
        else:
            op_piece = player1.piece

        # get valid columns to score
        valid_cols = []   
        for col in range(7):
            if board[0][col] == "_":
                valid_cols.append(col)
            else:valid_cols.append(-1)

        # get lowest row position for each  valid column to score
        first_available_row = []  
        for col in valid_cols:
            if int(col) != -1:
                for row in range(5,-1,-1):
                    if board[row][col] == "_":
                        first_available_row.append(row)
                        break
            else:
                first_available_row.append(0)
                
        # make  copy of the board, drops a piece in each playable position
        # and sends it to be scored
        for index in range(len(valid_cols)):  
            if valid_cols[index] != -1:      
                temp_board = copy.deepcopy(board)
                #i = 0  # use to fill the board with consequetive integers for testing
                #for r in range(0,6):
                    #for c in range(0,7):
                        #temp_board[r][c] = i
                        #i += 1
                temp_board[first_available_row[index]][valid_cols[index]] = "*"
                # stores the returned scores with a -1 value in full columns
                final_scores.append( player.scoring_function(temp_board,player,index, op_piece)) 
            else:
                final_scores.append(-1)

        col = final_scores.index(max(final_scores))
        return col



    def scoring_function(self, temp_board, player, col, op_piece):
        """ 
        Breaks the copy of the playing board into
        slices of 4 and sends them to be scored

        Parameters:
        temp_board: array - copy of the current board with an '*' placed in column to be scored

        player: object - representing the current player(computer)

        col: int - stores the current column being scored

        op_piece: str - the human players playing piece type

        Variables:
        score: int - stores the column being scored score

        row_array: array - stores a row of horizontal positions

        column_array: array - stores a row of vertical positions

        diagfor_array: array - stores a row of forward leaning positions

        diagback_array: array - stores a row of backward leaning positions

        Returns:
        score: int - the column's score.
        """
        score = 0
        for i in range(5, -1,-1): # score rows do each row in turn in blocks of 4
            row_array = list(temp_board[i])
            for j in range(4):
                slice4 = row_array[j:j+4]
            
                score += self.scoring_logic(player, slice4, col, op_piece)

        # check column for line of 4
        for i in range(7):
            column_array = []
            for j in range(5, -1,-1):
                t = temp_board[j][i]
                column_array.append(t)
            for j in range(3):
                slice4 = column_array[j:j+4]
                

                score += self.scoring_logic(player, slice4, col, op_piece)

        # forwards diagonals scoring

        # left half of board
        for i in range(3,6):
            diagfor_array = []
            for p in range(i + 1):
                t = temp_board[i-p][p]
                diagfor_array.append(t)
            for j in range(len(diagfor_array)-3):
                slice4 = diagfor_array[j:j+4]
                score += self.scoring_logic(player, slice4, col, op_piece)

     
                
                
        # backwards diagonals scoring
        for i in range(3, 6):
            diagback_array = []
            for p in range(i + 1):
                t = temp_board[(i - p)][6 - p]
                diagback_array.append(t)
            for j in range(len(diagback_array)-3):
                slice4 = diagback_array[j:j+4]   
                
                score += self.scoring_logic(player, slice4, col, op_piece)

        return score
             

    def scoring_logic(self, player, slice4, col, op_piece):
        """ 
        Scores each slice of 4 

        Parameters:
        player: object - representing the computer player

        slice4: array - the list of four position being scored

        col: int - the column being scored

        op_piece: str - the human player's piece type

        Variables:
        score: int - the slices score

        Returns:
        score: int - the slices score.
        
        """
        score = 0 
        if slice4.count(player.piece) == 4: # this is redundant now remove check!
            score+= 10000
        elif slice4.count(player.piece) == 3 and slice4.count("*") == 1:
            score += 2000
        elif slice4.count(player.piece) == 2 and slice4.count("*") == 1:
            score += 1000
        elif slice4.count(player.piece) == 1 and slice4.count("_") == 3:
            score += 100  
        elif col == 3:
            score += 50

        # blocking moves
        if slice4.count(op_piece) == 3 and slice4.count("*") == 1:
            score += 10000
        if slice4.count(op_piece) == 3 and slice4.count("_") == 1:
            score += 2000
        if slice4.count(op_piece) == 2: # and slice4.count("_") >= 1:
            score += 1500
        if slice4 == ["*", op_piece, op_piece, "_"] or slice4 == ["-", op_piece, op_piece, "*"]:
            score += 5000

        return score
