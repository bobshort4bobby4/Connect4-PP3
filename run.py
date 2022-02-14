import random

from classes.player import PLAYER
from classes.board import Board



def play_game():
    game = Board()
    game_over = False
    player1 = {} 
    player2 = {}
    player1, player2 = PLAYER.determine_first(player1, player2, game)
    level = "medium"

    while not game_over:
        player = game.whose_turn(player1,player2)
        choice, piece_type = game.take_move(player, level)
        game.insert_piece(choice, piece_type)
        game.draw_board()
        game_over = game.check_draw(game.board)
        game_over = game.check_win(game.board, player)
        

    if game.play_again():
        play_game()
   

if __name__ == '__main__':
    play_game()
