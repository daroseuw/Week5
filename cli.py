# # This file contains the Command Line Interface (CLI) for
# # the Tic-Tac-Toe game. This is where input and output happens.
# # For core game logic, see logic.py.

from logic import Board, Players, Moves, GameRules, RunGame

# # Prep:
#     # Get a new board
#     # See who will go first: establish current player
#     # Phase 2: Human or AI?
#     # 
# # Gameplay
#     # Make sure there isn't already a winner
#     # Prompt the first player to make a move
#     # Update the board if the move was valid, otherwise ask again
#     # Switch to next player and repeat previous steps
#     # Declare a winner or a draw
#     # Option to start a new game

# try:
#     if __name__ == '__main__':
#         board = None # Need to refactor board dependency
#         current_player = None
#         winner = False

        
#         while winner == None:
            
#             board = Board()
#             board.new_board()
#             board.print_board()
#             players = Players()
#             current_player = players.get_first_player()
#             players.get_first_player_name()
#             players.get_second_player()
#             players.get_second_player_name()
#             # print(current_player)

#             # TODO: Show the board to the user.

#             # TODO: Input a move from the player.
#             game = GameRules()
#             moves = Moves()
#             # winner = game.
#             while winner == False and game.board_full 

#             # move = PlayerInteraction()
#             # move.get_move(game_board.board)
#             # TODO: Update the board.

#             # TODO: Update who's turn it is.

#             # winner = '_'
# except:
#     print("An error has occurred.")

rungame = RunGame()
rungame.gameplay()