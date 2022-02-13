import random

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ColumnFullError(Error):
    """Raised when the column is full"""
    pass

class PLAYER:
    """
    the players of the game
    """

    def __init__(self, name,piece):
        self.name = name
        self.piece = piece

    @staticmethod
    def determine_first():
        first = random.randint(1, 2)
        return first



class Board():
    """
    build the board the game is played on
    """
    def __init__(self):
        self.board = self.build()
        self.number_turns = 2
        

    def build(self):
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
        print("")
        print("    0 1 2 3 4 5 6 ")
        print("__________________")
        for i in range(6):
                print(i, "~", end="|")
                for j in range(7):
                        print(self.board[i][j], end="|")
                print("")
                
    def whose_turn(self, player1, player2):
        if self.number_turns % 2 == 0:
            player = player1
            self.number_turns += 1
        else:
            player = player2
            self.number_turns += 1
        return player

    def take_move(self, player ):
        col = 11
        if player.name == "Computer":
            invalid_col = True
            while invalid_col:
                col = random.randint(0,6)
                if self.board[0][col] == "_":
                    invalid_col = False
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
        for row in range(5, -1, -1):
            if self.board[row][choice] == "_":
                self.board[row][choice] = player_piece
                break
        return

    def check_draw(self, board):
        strboard = str(board)
        temp = strboard.count("_")
        if temp > 0:
            return False
        else:
            print(" The game is a DRAW! Human hang your head in SHAME.")
            return True


    def check_win(self, board, player):
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



def play_game():
    game = Board()
    game_over = False
    first= PLAYER.determine_first()
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

    while not game_over:
        player = game.whose_turn(player1,player2)
        choice, piece_type= game.take_move(player)
        game.insert_piece(choice, piece_type)
        game.draw_board()
        game_over = game.check_draw(game.board)
        game_over = game.check_win(game.board, player)
        

    
   

if __name__ == '__main__':
    play_game()
