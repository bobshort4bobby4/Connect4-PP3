"""
Module containing the class to create, track and manipulate the game state

Classes: Board
"""
import pyfiglet
from classes import CustomError
from classes.ClearMixin import ClearMixin


class Board(ClearMixin):
    """
    Builds the board the game is played on
    and methods to play game

    Parameters:
    ClearMixin: Class - clears the terminal screen

    Methods:
    def build(): creates the 2d array to represent the playing board

    def draw_board(): draws the current state of the
                                 play-board to the terminal screen

    def display_intro(): displays the introduction screen and
                                         returns  user choice of difficulty

    def whose_turn(): determines which player should take next turn

    def take_move(): Determines/accepts th players move and returns it

    def insert_piece(): places the appropriate piece in the
                                    correct position in the board array

    def check_draw(): checks the current play-board for a drawn state

    def check_win(): checks if the current player has won
                                     the game and if so displays a message.

    def play_again(): determines if the player wishes
                         to play again, if not, exits the game
    """

    def __init__(self):
        """
        Constructs the attributes for the Board object.

        Attributes:
        board: array - the 2d array used to represent the game-board

        number_turns: int - used to determine which player plays next

        game_over: boolean - used to signal the end of a game cycle
        """
        self.board = self.build()
        self.number_turns = 2
        self.game_Over = False

    def build(self):
        """
        Creates the 2d array to represent the board

        Variables:
        board_width: int - the width of the playing board
                                             measured in playing pieces

        board_height: int - the height of the playing board
                                             measured in playing pieces

        Returns:
        board: array - the playing board.
        """

        board_width = 7
        board_height = 6
        # create empty array
        self.board = []
        for i in range(board_width - 1):
            self.board.append([])
        # fill board object
        for i in range(board_height):
            for j in range(board_width):
                self.board[i].insert(j, "_")
        return self.board

    def draw_board(self):
        """
        Draws the current state of game to screen using the current board

        Variables:
        board: array - the playing board

        Returns: none.
        """

        self.clrscr()
        print("")
        print("                                   0 1 2 3 4 5 6 ")
        print("                               __________________")
        for i in range(6):
                print("                              ", i, "~", end="|")
                for j in range(7):
                        print(self.board[i][j], end="|")
                print("")

    def display_intro(self):
        """
        Displays intro screen and takes difficulty level from user

        Variables:
        ans:int - stores the input from user to set the difficulty level

        level: str - stores the difficulty level
        question2: str - used to store string formatted
                                         using the Pyfiglet library

        question3: str - used to store string formatted
                                         using the Pyfiglet library

        question4: str - used to store string formatted
                                         using the Pyfiglet library

        cond: boolean - used to control input loop

        Returns:
        level
        """

        self.clrscr()
        # change colour
        print('\033[93m')
        title = pyfiglet.figlet_format("                  Connect 4")
        print(title)
        print("  A version of the classic board game 'Connect4'," +
              "first sold in 1974.")
        print("  There are over 4.5 trillion combinations " +
              "of tiles possible on the ")
        print("  standard 6 by 7 board.")
        print("  The object of the game is to connect " +
              "four of your colour tiles in a")
        print("  line, the  line can be in any direction.")
        print("  If all the pieces are used before a line is " +
              "found the game is a draw")

        input("  Press Enter To Continue...\n")

        self.clrscr()

        question2 = pyfiglet.figlet_format(" 1. Easy ")
        question3 = pyfiglet.figlet_format(" 2. Medium")
        question4 = pyfiglet.figlet_format(" 3. Hard")
        # print("THREE DIFFICULTY LEVELS ARE AVAILABLE ")
        print(question2, question3, question4)
        cond = True

        # takes in amd validates level from the user
        while cond:
            try:
                ans = int(input("Enter 1 for Easy, " +
                                "2 for Medium or 3 for Hard :\n"))
                if type(int(ans)) is int and ans == 1 or ans == 2 or ans == 3:
                    cond = False
                if ans != 1 and ans != 2 and ans != 3:
                    raise ValueError("Please select either 1, 2 or 3.")
                if not type(ans) is int:
                    raise TypeError("Only integers are allowed")

            except TypeError:
                print("Please enter the digit 1," +
                      "the digit 2 or the digit 3. ")
            except ValueError:
                print("Please enter the digit 1," +
                      "the digit 2 or the digit 3.")

        # change back to default colour
        print('\033[39m')
        # sets difficulty level variable to correct value
        if int(ans) == 1:
            level = "easy"
        elif int(ans) == 2:
            level = "medium"
        else:
            level = "hard"

        return level

    def whose_turn(self, player1, player2):
        """
         Determines whose turn it is and returns the answer

         Parameters:
         player1: instance of Class Player

         player2: instance of Class Player

         Variables:
         player: object representing either player1 or player2

         Returns:
         player: object representing either player1 or player2
        """

        if self.number_turns % 2 == 0:
            player = player1
            self.number_turns += 1
        else:
            player = player2
            self.number_turns += 1
        return player

    def take_move(self, player, level, player1, player2):
        """
        Determines which column the current player
        wants to play and returns it,
        updates the player_moves variable

        Parameters:
        player: object - reprsenting the current player

        level: str - the difficulty level for the current game

        player1: instance of Player Class - player1

        player2: instance of Player class - player2

        Variables:
        col: int - the column the player picks to play

        Returns:
        col: int - the column the player picks to play

        player.piece: object attribute - the current players piece type.
        """
        player.player_moves += 1
        col = 11
        # code for computer player
        if player.name == "Computer":
            if level == "easy":
                # calls easy level logic
                col = player.computer_move_random(self.board)
                return col, player.piece
            elif level == "medium" or level == "hard":
                # calls medium level logic
                col = player.computer_move_scored(
                    player, self.board, player1, player2, level)
                return col, player.piece
        # set col to invalid value to ensure while loop is run at least once
        col = 11
        # takes in players choice of column and validates it
        new_line = '\n'
        while(col < 0) or(col > 6):
            try:
                print("")
                print(player.name, "!")
                col = int(input(
                    f"Pick a column to drop an {player.piece}{new_line}"))

                if col < 0 or col > 6:
                    # checks if input number is within valid range
                    raise IndexError("  between 0 and 6")
                # checks if the column is full
                if self.board[0][col] != "_":
                    col = 11
                    raise CustomError.ColumnFullError

            except ValueError:
                    print("Enter a NUMBER in range 0-6")

            except CustomError.ColumnFullError:
                    print("Column full")

            except IndexError:
                    print("  Enter a NUMBER in range 0-6")

        return col, player.piece

    def insert_piece(self, choice, player_piece):
        """
         Inserts the piece into the board array

         Parameters:
         choice: int - the column the playing piece is to dropped in

         player_piece: str - the type of playing piece to be used

         Returns: None.

        """

        for row in range(5, -1, -1):
            # drops the correct piece into the first empty row of the column
            if self.board[row][choice] == "_":
                self.board[row][choice] = player_piece
                break
        return

    def check_draw(self, board, player):
        """
        Checks to see if the game is drawn, displays a messsage
        and toggles the game.game_over attribute if so

        Paramaters:
        board: object attribute - the playing board

        player: object - representing the current player

        Variables:
        strboard: str - the game board represented as a string,
        used to count number of empty positions left

        temp: int - the number of empty spaces in the current board

        Returns: None.
        """
        strboard = str(board)
        temp = strboard.count("_")
        # if any empty positions remaining set
        #  game.game_over to false else set to true
        if temp > 0:
            self.game_Over = False
        else:
            print("The game is a DRAW!.")
            print(f"You have taken {player.player_moves} moves in this game")
            self.game_Over = True

    def check_win(self, board, player):
        """
        Checks if game is won by sectioning each block
        of 4 position and checking for four of the same
        type piece in all positions,
        toggles game.game_over attribute if game won

        Parameters:
        board: object attribute - the current state of the playing board

        player: object - representing the current player

        Variables:
        player.piece: object attribure - the current
            players type of playing piece

        Returns: None.
        """

        # break rows into blocks of four, check if all are the player's piece
        #  and if so colour them red and set game_over to true
        for i in range(6):
            for j in range(4):
                if (self.board[i][j] == player.piece and
                        self.board[i][j+1] == player.piece and
                        self.board[i][j+2] == player.piece and
                        self.board[i][j+3] == player.piece):
                    self.board[i][j] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[i][j+1] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[i][j+2] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[i][j+3] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won! "
                          f"Congratulations {player.name}")
                    print(f"{player.name}! "
                          f"You have taken {player.player_moves} moves"
                           " in this game" + '\033[39m')
                    self.game_Over = True

        # break columns into blocks of four,
        # check if all are the player's piece
        # and if so colour them red and set game_over to true
        for i in range(7):
            for j in range(3):
                if (self.board[j][i] == player.piece and
                        self.board[j + 1][i] == player.piece and
                        self.board[j + 2][i] == player.piece and
                        self.board[j + 3][i] == player.piece):
                    self.board[j][i] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[j+1][i] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[j+2][i] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[j+3][i] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won! "
                          f"Congratulations {player.name}")
                    print(f"{player.name}! "
                          f"You have taken {player.player_moves} moves"
                           " in this game" + '\033[39m')
                    self.game_Over = True

        # break forward diagonals into blocks of four,
        # check if all are the player's piece and if so
        # colour them red and set game.over to true
        for i in range(3, 6):
            for j in range(0, 4):
                if (self.board[i][j] == player.piece and
                        self.board[i-1][j+1] == player.piece and
                        self.board[i-2][j+2] == player.piece and
                        self.board[i-3][j+3] == player.piece):
                    self.board[i][j] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[i-1][j+1] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[i-2][j+2] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.board[i-3][j+3] = '\033[31m' + player.piece + \
                        '\033[39m'
                    self.draw_board()
                    print('\033[0;32m' + f"{player.piece} has won! "
                          f"Congratulations {player.name}")
                    print(f"{player.name}! "
                          f"You have taken {player.player_moves} moves"
                           " in this game" + '\033[39m')
                    self.game_Over = True

        # break backwards diagonals into blocks of four, check if all are
        # the player's piece and if so colour them red and
        #  set game_over to true

        for i in range(3, 6):
            for j in range(6, 2, -1):
                if (self.board[i][j] == player.piece and
                        self.board[i-1][j-1] == player.piece and
                        self.board[i-2][j-2] == player.piece and
                        self.board[i-3][j-3] == player.piece):

                        self.board[i][j] = '\033[31m' + player.piece + \
                            '\033[39m'
                        self.board[i-1][j-1] = '\033[31m' + player.piece + \
                            '\033[39m'
                        self.board[i-2][j-2] = '\033[31m' + player.piece + \
                            '\033[39m'
                        self.board[i-3][j-3] = '\033[31m' + player.piece + \
                            '\033[39m'
                        self.draw_board()
                        print('\033[0;32m' + f"{player.piece} has won! "
                              f"Congratulations {player.name}")
                        print(f"{player.name}! "
                              f"You have taken {player.player_moves} moves"
                              " in this game" + '\033[39m')
                        self.game_Over = True

    def play_again(self):
        """
        Asks the user  if they want to play again
        returns true if user wants to play again, exit the program if not

        Parameters: None

        Variables:
        ans: str - used to store the user input regarding play or exit

        lowerans: str - the ans variable in lower case

        valid_input: boolean - used to control input/validation process

        bye: str - used to store farewell message

        Returns: boolean (true) - if user wishes to play again,
         exits the program if not
         """

        ans = ""
        valid_input = False
        # accepts user input and validates it
        while not valid_input:
            ans = input(
                        "Enter 'quit' to finish or" +
                        " 'again' to play again :\n")
            lowerans = ans.lower()
            # if user wants to quit print messsage and exit
            if lowerans == "quit":
                valid_input = True
                print('\033[31m')
                bye = pyfiglet.figlet_format("                     BYE BYE  ")
                print(bye)
                print('\033[39m')
                print("                    THANKS FOR " +
                      "PLAYING C4 IT'S BEEN A BLAST!")
                exit()
            elif lowerans == "again":
                # if user wants to play again return true
                valid_input = True
        return True
