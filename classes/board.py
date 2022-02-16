import sys
import pyfiglet
path_to_module = "classes/"
sys.path.append(path_to_module)
from error import *
from ClearMixin import *


class Board(ClearMixin):
    """
    build the board the game is played on
    and methods to play game
    """
    def __init__(self):
        self.board = self.build()
        self.number_turns = 2
        self.game_Over = False
        
        
    def build(self):
        """ 
        creates the 2d array to represent the board
        """

        board_width = 7
        board_height = 6
        self.board = [] # create empty array
        for i in range(board_width - 1):
            self.board.append([])

        for i in range(board_height):  # fill board object
            for j in range(board_width):
                self.board[i].insert(j, "_")
        return self.board


    def draw_board(self):
        """ 
        draws the current state of game to screen
        """

        self.clrscr()
        print("")
        print( "                                   0 1 2 3 4 5 6 ")
        print( "                               __________________")
        for i in range(6):
                print("                              ",i, "~", end="|")
                for j in range(7):
                        print(self.board[i][j], end="|")
                print("")


    def display_intro(self):
        """
        displays intro screen and takes difficulty level from user
        returns level
        """

        self.clrscr()
        player1 = {}
        player2 = {}
        print('\033[93m') # change colour
        title = pyfiglet.figlet_format( "                    Connect 4")
        print(title)
        print("  A version of the classic board game 'Connect4', first sold in 1974.")
        print("  There are over 4.5 trillion combinations of tiles possible on the ")
        print("  standard 6 by 7 board.")
        print("  The object of the game is to connect four of your colour tiles in a")
        print("  line, the  line can be in any direction.")
        print("  If all the pieces are used before a line is found the game is a draw")
        
        input("  Press Enter To Continue...\n")

        self.clrscr()
        question = pyfiglet.figlet_format("   Two difficulty levels are provided " )
        question2 = pyfiglet.figlet_format(" 1. Easy ")
        question3 = pyfiglet.figlet_format(" 2. Medium")
        print("TWO DIFFICULTY LEVELS ARE AVAILABLE ")
        print(question2, question3)
        cond = True  
        while cond: # takes in amd validates level from the user
            try:
                ans = int(input("Enter 1 for Easy or 2 for Medium :\n"))
                if type(int(ans)) is int and ans == 1 or ans == 2:
                    cond = False
                if not type(ans) is int:
                    raise TypeError("Only integers are allowed")
                
            except TypeError:
                print("Please the digit 1 or the digit 2 ")
            except ValueError:
                print("Please the digit 1 or the digit 2 ")
            
        print('\033[39m') # change back to default clour
      
        if int(ans) == 1: # sets difficulty level variable to correct value
            level = "easy"
        else:
            level = "medium"

        return level

       
    def whose_turn(self, player1, player2):
        """
         determines whose turn it is and returns the answer
         """

        if self.number_turns % 2 == 0:
            player = player1
            self.number_turns += 1
        else:
            player = player2
            self.number_turns += 1
        return player


    def take_move(self, player, level, player1, player2 ):
        """
         determines what column the player wants to play and returns it
         """

        col = 11
        if player.name == "Computer": # code for computer player
            if level == "easy":
                col = player.computer_move_random(self.board) # calls easy level logic
                return col, player.piece
            elif level == "medium":
                col = player.computer_move_scored(player, self.board, player1, player2) # calls medium level logic
                return col, player.piece

        col = 11
        while(col < 0) or(col > 6):  # takes in players choice of column and validate it
            try:
                print("")
                col = int(input(f"  {player.name} pick a column to drop an {player.piece} "))
                                
                if col < 0 or col > 6:
                    raise IndexError("  between 0 and 6") # checks if input number is within valid range
                if self.board[0][col] != "_":  # checks if the column is full
                    col = 11
                    raise ColumnFullError

            except ValueError:
                    print("  Enter a NUMBER in range 0-6")
           
            except ColumnFullError:
                    print("  Column full")
                    
            except IndexError:
                    print("  Enter a NUMBER in range 0-6")
                 
        return col, player.piece



    def insert_piece(self, choice, player_piece):
        """
         inserts the piece into the aboard array
        """

        for row in range(5, -1, -1):
            if self.board[row][choice] == "_": # drops the correct piece into the first empty row of the choosen column
                self.board[row][choice] = player_piece
                break
        return


    def check_draw(self, board):
        """ 
        checks to see if the game is drawn and returns a boolean
        """
        strboard = str(board)
        temp = strboard.count("_")
        if temp > 0:      # if any empty positions remaining return false else return true
            return False
        else:
            print("  The game is a DRAW! Human hang your head in SHAME.")
            return True


    def check_win(self, board, player):
        """
        checks if game is won and returns a boolean
        """
       
        # break rows into blocks of four, check if all are the player's piece and if so colour them red and return true                    
        for i in range(6): 
            for j in range(4):
                if self.board[i][j] == player.piece and self.board[i][j+1] == player.piece and self.board[i][j+2] == player.piece and self.board[i][j+3] == player.piece:
                    self.board[i][j] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i][j+1] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i][j+2] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i][j+3] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"  {player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True
    
        # break columns into blocks of four, check if all are the player's piece and if so colour them red and return true
        for i in range(7):
            for j in range(3):
                if self.board[j][i] == player.piece and self.board[j + 1][i] == player.piece and self.board[j + 2][i] == player.piece and self.board[j + 3][i] == player.piece:
                    self.board[j][i] = '\033[31m' + player.piece + '\033[39m'
                    self.board[j+1][i] = '\033[31m' + player.piece + '\033[39m'
                    self.board[j+2][i] = '\033[31m' + player.piece + '\033[39m'
                    self.board[j+3][i] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"  {player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True

        # break forward diagonals into blocks of four, check if all are the player's piece and if so colour them red and return true
        for i in range(3,6):
            for j in range(0,4):
                if self.board[i][j] == player.piece and self.board[i-1][j+1] == player.piece and self.board[i-2][j+2] == player.piece and self.board[i-3][j+3] == player.piece:
                    self.board[i][j] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-1][j+1] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-2][j+2] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-3][j+3] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"  {player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True

        # break backwards diagonals into blocks of four, check if all are  the player's piece and if so colour them red and return true

        for i in range(3,6):
            for j in range(6,2,-1):
                if board[i][j] == player.piece and self.board[i-1][j-1] == player.piece and self.board[i-2][j-2] == player.piece and self.board[i-3][j-3] == player.piece:
                    self.board[i][j] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-1][j-1] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-2][j-2] = '\033[31m' + player.piece + '\033[39m'
                    self.board[i-3][j-3] = '\033[31m' + player.piece + '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"  {player.piece} has won!  Congratulations {player.name}" + '\033[39m' )
                    return True


    def play_again(self):
        """ 
        asks for user input if they want to play again
        returns true if user wants to play again
         """

        # print("  Enter 'Quit' to finish or 'again' to play again")
        ans = ""
        valid_input = False
        while not valid_input: # accepts user input and validates it
            ans = input("  Enter 'Quit' to finish or 'again' to play again : \n")
            lowerans = ans.lower()
            if lowerans == "quit": # if user wants to quit print messsage and exit
                valid_input = True
                print('\033[31m')
                bye = pyfiglet.figlet_format("             BYE BYE  ")
                print(bye)
                print('\033[39m')
                print("                        THANKS FOR PLAYING C4 IT'S BEEN A BLAST!")
                exit()
            elif lowerans == "again":
                valid_input = True # if user wants to play again return true 
        return True
        