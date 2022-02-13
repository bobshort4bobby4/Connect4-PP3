import random

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