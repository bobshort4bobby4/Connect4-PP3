""" 
Controls game flow and creates instances of the Board (1) and Player (2) Classes

Functions:
play_game

Returns: None.
"""
import random
from classes.player import Player
from classes.board import Board


def play_game():
    """ 
    Controls program flow and creates instances of the Board (1) and Player (2) Classes

    Variables:
    game: Object - instance of the Board Class
    player1: Object - instance of the Player Class
    player2: Object - instance of the Player Class
    level: int - the difficulty level the player has choosen
    choice: int - the column number the current player has choosen to drop piece in
    piece_type: str - the current players piece type


    Returns: None.
    """

    game = Board()
    player1, player2, level = Player.init_game(game)

    while not game.game_Over:
        player = game.whose_turn(player1,player2)
        choice, piece_type = game.take_move(player, level, player1, player2)
        game.insert_piece(choice, piece_type)
        game.draw_board()
        game.check_draw(game.board)
        game.check_win(game.board, player)
        
    if game.play_again():
        play_game()
   

if __name__ == '__main__':
    play_game()
