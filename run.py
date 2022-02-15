
import random
from classes.player import PLAYER
from classes.board import Board



def play_game():
    game = Board()
    player1, player2, level = PLAYER.init_game(game)

    while not game.game_Over:
        player = game.whose_turn(player1,player2)
        choice, piece_type = game.take_move(player, level, player1, player2)
        game.insert_piece(choice, piece_type)
        game.draw_board()
        game.game_Over = game.check_draw(game.board)
        game.game_Over = game.check_win(game.board, player)
        

    if game.play_again():
        play_game()
   

if __name__ == '__main__':
    play_game()
