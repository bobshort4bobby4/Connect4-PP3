import sys
path_to_module = "classes/"
sys.path.append(path_to_module)
from error import *

class Board():
    """
    build the board the game is played on
    and methods to play game
    """
    def __init__(self):
        self.board = self.build()
        self.number_turns = 2
        

    def build(self):
        """ creates the 2d array to represent the board"""

        board_width = 7
        board_height = 6
        self.board = []
        for i in range(board_width - 1):
            self.board.append([])

        for i in range(board_height):  # fill board variable
            for j in range(board_width):
                self.board[i].insert(j, "_")
        return self.board

    def draw_board(self):
        """ draws the current state of game to screen"""

        print("")
        print( "               0 1 2 3 4 5 6 ")
        print( "           __________________")
        for i in range(6):
                print("          ",i, "~", end="|")
                for j in range(7):
                        print(self.board[i][j], end="|")
                print("")
                
    def whose_turn(self, player1, player2):
        """ determines whose turn it is and returns the answer"""

        if self.number_turns % 2 == 0:
            player = player1
            self.number_turns += 1
        else:
            player = player2
            self.number_turns += 1
        return player

    def take_move(self, player ):
        """ determines what column the player wants to play and returns it"""

        col = 11
        if player.name == "Computer":
            col = player.computer_move_random(self.board)
            return col, player.piece

        col = 11
        while(col < 0) or(col > 6):
            try:
                col = int(input(f"{player.name} pick a column to drop an {player.piece}: "))
                                
                if col < 0 or col > 6:
                    raise IndexError("between 1 and 6")
                if self.board[0][col] != "_":
                    col = 11
                    raise ColumnFullError

            except ValueError:
                    print("Enter a NUMBER in range 0-6")
           
            except ColumnFullError:
                    print("column full")
                    
            except IndexError:
                    print("Enter a NUMBER in range 0-6")
                 
        return col, player.piece

    def insert_piece(self, choice, player_piece):
        """ inserts the piece into the aboard array"""

        for row in range(5, -1, -1):
            if self.board[row][choice] == "_":
                self.board[row][choice] = player_piece
                break
        return

    def check_draw(self, board):
        """ checks to see if the game is drawn and returns a boolean"""

        strboard = str(board)
        temp = strboard.count("_")
        if temp > 0:
            return False
        else:
            print(" The game is a DRAW! Human hang your head in SHAME.")
            return True


    def check_win(self, board, player):
        """ checks if game is won and returns a boolean"""
        
        print("in checkwin  function piece is ", player.piece)
    #check rows for line of 4
        temp  = 0
        for i in range(6): 
            for j in range(4):
                if self.board[i][j] == player.piece and self.board[i][j+1] == player.piece and self.board[i][j+2] == player.piece and self.board[i][j+3] == player.piece:
                    self.board[i][j] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i][j+1] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i][j+2] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i][j+3] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True

    # check column for line of 4

        for i in range(7):
            for j in range(3):
                if self.board[j][i] == player.piece and self.board[j + 1][i] == player.piece and self.board[j + 2][i] == player.piece and self.board[j + 3][i] == player.piece:
                    self.board[j][i] = '\033[31m' + player.piece + '\033[39m'
                    self.board[j+1][i] = '\033[31m' + player.piece + '\033[39m'
                    self.board[j+2][i] = '\033[31m' + player.piece + '\033[39m'
                    self.board[j+3][i] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True

    # check forwards  diagonals for line of 4
   
        for i in range(3,6):
            for j in range(0,4):
                if self.board[i][j] == player.piece and self.board[i-1][j+1] == player.piece and self.board[i-2][j+2] == player.piece and self.board[i-3][j+3] == player.piece:
                    self.board[i][j] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-1][j+1] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-2][j+2] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-3][j+3] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True

    # check backwards diagonals for line of 4 

        for i in range(3,6):
            for j in range(6,2,-1):
                if board[i][j] == player.piece and self.board[i-1][j-1] == player.piece and self.board[i-2][j-2] == player.piece and self.board[i-3][j-3] == player.piece:
                    self.board[i][j] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-1][j-1] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-2][j-2] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-3][j-3] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True