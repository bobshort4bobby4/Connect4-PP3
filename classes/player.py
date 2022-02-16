import random
import sys
import copy
import time
path_to_module = "classes/"
sys.path.append(path_to_module)
from ClearMixin import *

class PLAYER(ClearMixin):
    """
    the players of the game
    """

    def __init__(self, name,piece):
        self.name = name
        self.piece = piece
    
    @staticmethod
    def init_game(game):

        """
        Function to decide which player starts,
        display intro screen
        and take user input re difficulty level
        returns both player objects and level variable
        """
        pause = 2
        level = game.display_intro()
        first = random.randint(1, 2) # decides play order, creates players
        if first == 1:
            player1 = PLAYER("Human", "x")
            player2 = PLAYER("Computer", "0")
            print( "\033[5;31m" + "Human to go first" + '\033[39m')
            time.sleep(pause)
        else:
            player1 = PLAYER("Computer", "x")
            player2 = PLAYER("Human", "0")
            print( "\033[5;31m" + "\033[5m" + " Computer to go first" + '\033[39m' )
            time.sleep(pause)
        
        ClearMixin().clrscr()
        game.draw_board()
        return player1, player2, level


    def computer_move_random (self,board):
        """
        generates totally random computer moves
        returns column choice
        """

        invalid_col = True
        while invalid_col:
            col = random.randint(0,6)
            if board[0][col] == "_":
                invalid_col = False
        return col


    def computer_move_scored(self, player, board,player1, player2):
        """ 
        Generates computer moves based on a simple position scoring system
        returns column choice
        """
        final_scores = []
        if player.piece == player1.piece: # get opposing piece to implement blocking move scoring 
            op_piece = player2.piece
        else:
            op_piece = player1.piece

        valid_cols = []   # get valid columns to score
        for col in range(7):
            if board[0][col] == "_":
                valid_cols.append(col)
            else:valid_cols.append(-1)

        first_available_row = []  # get lowest row position for each  valid column to score
        for col in valid_cols:
            if int(col) != -1:
                for row in range(5,-1,-1):
                    if board[row][col] == "_":
                        first_available_row.append(row)
                        break
            else:
                first_available_row.append(0)
                
        for index in range(len(valid_cols)): # make  copy of the board, drops a piece in each playable position 
            if valid_cols[index] != -1:      # and sends it to be scored
                temp_board = copy.deepcopy(board)
                temp_board[first_available_row[index]][valid_cols[index]] = player.piece
                final_scores.append( player.scoring_function(temp_board,player,index, op_piece)) # stores the returned scores with a -1 value in full columns
            else:
                final_scores.append(-1)

        col = final_scores.index(max(final_scores))
        return col



    def scoring_function(self, temp_board, player, col, op_piece):
        """ 
        scores each position in the temporary board
        returns the score for that board
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
        scores each slice of 4 
        returns the update for the score variable for the current column
        """
        score = 0 
        if slice4.count(player.piece) == 4:
            score+= 2000
        elif slice4.count(player.piece) == 3 and slice4.count("_") == 1:
            score += 1200
        elif slice4.count(player.piece) == 2 and slice4.count("_") > 1:
            score += 800
        elif slice4.count(player.piece) == 1 and slice4.count("_") == 3:
            score += 10  
        elif col == 3:
            score += 5
            
        # blocking moves
        if slice4.count(op_piece) == 3 and slice4.count(player.piece) == 1:
            score += 2000
        if slice4.count(op_piece) == 3 and slice4.count("_") == 1:
            score += 2000
        if slice4 == ["_", op_piece, op_piece, "_"]:
            score += 250

        return score
