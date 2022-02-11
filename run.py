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
                col = random.randint(0,7)
            return col

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
                 
        return col






def play_game():
    game = Board()
    game_over = False
    first= PLAYER.determine_first()
    if first == 1:
        player1 = PLAYER("Human", "x")
        player2 = PLAYER("Computer", "0")
        print("Human to go first")
    else:
        player1 = PLAYER("Computer", "x")
        player2 = PLAYER("Human", "0")
        print("Computer to go first")


    while not game_over:
        player = game.whose_turn(player1,player2)
        choice = game.take_move(player)
        game_over =True

    
    game.draw_board()

if __name__ == '__main__':
    play_game()
