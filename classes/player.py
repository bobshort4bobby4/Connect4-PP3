import random
import copy
class PLAYER:
    """
    the players of the game
    """

    def __init__(self, name,piece):
        self.name = name
        self.piece = piece

    @staticmethod
    def determine_first(player1,player2, game):
        first = random.randint(1, 2)
        if first == 1:
            player1 = PLAYER("Human", "x")
            player2 = PLAYER("Computer", "0")
            print( "\033[5;31m" + "Human to go first" + '\033[39m')
        else:
            player1 = PLAYER("Computer", "x")
            player2 = PLAYER("Human", "0")
            print( "\033[5;31m" + "\033[5m" + " Computer to go first" + '\033[39m' )

        if player1.name == "Human":
            game.draw_board()
        
        return player1, player2

    def computer_move_random (self,board):
        invalid_col = True
        while invalid_col:
            col = random.randint(0,6)
            if board[0][col] == "_":
                invalid_col = False
        return col

    def computer_move_scored(self, player, board,player1, player2):
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
            for row in range(5,-1,-1):
                if board[row][col] == "_":
                    first_available_row.append(row)
                    break
                

        
        for index in range(len(valid_cols)):
            if valid_cols[index] != -1:
                temp_board = copy.deepcopy(board)
                temp_board[first_available_row[index]][valid_cols[index]] = player.piece
                final_scores.append( player.scoring_function(temp_board,player,index, op_piece))
            else:
                final_scores.append(-1)

        col = final_scores.index(max(final_scores))
        return col

    def scoring_function(self, temp_board, player, col, op_piece):
        score = 0
        for i in range(5, -1,-1): # score rows do each row in turn in blocks of 4
            row_array = list(temp_board[i])
            for j in range(4):
                slice4 = row_array[j:j+4]
                if slice4.count(player.piece) == 4:
                    score+= 200
                elif slice4.count(player.piece) == 3 and slice4.count("_") == 1:
                    score += 150
                elif slice4.count(player.piece) == 2 and slice4.count("_") > 1:
                    score += 25
                elif col == 3:
                    score += 10
                elif slice4.count(player.piece) == 1 and slice4.count("_") == 3:
                    score += 10
                if slice4.count(op_piece) == 3 and slice4.count(player.piece) == 1:
                    score += 1900
        # check column for line of 4

        for i in range(7):
            column_array = []
            for j in range(5, -1,-1):
                t = temp_board[j][i]
                column_array.append(t)
            for j in range(3):
                slice4 = column_array[j:j+4]
                if slice4.count(player.piece) == 4:
                    score+= 200
                elif slice4.count(player.piece) == 3 and slice4.count("_") == 1:
                    score += 150
                elif slice4.count(player.piece) == 2 and slice4.count("_") > 1:
                    score += 25
                elif col == 3:
                    score += 10
                elif slice4.count(player.piece) == 1 and slice4.count("_") == 3:
                    score += 10  
                if slice4.count(op_piece) == 3 and slice4.count(player.piece) == 1:
                    score += 1900
            # for j in range(3):
                # if self.board[j][i] == player.piece and self.board[j + 1][i] == player.piece and self.board[j + 2][i] == player.piece and self.board[j + 3][i] == player.piece:  
                    
        return score
                # if self.board[i][j] == player.piece and self.board[i][j+1] == player.piece and self.board[i][j+2] == player.piece and self.board[i][j+3] == player.piece:


