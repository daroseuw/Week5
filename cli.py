# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

# Prep:
    # Get a new board
    # See who will go first: establish current player
    # Phase 2: Human or AI?
    # 
# Gameplay
    # Make sure there isn't already a winner
    # Prompt the first player to make a move
    # Update the board if the move was valid, otherwise ask again
    # Switch to next player and repeat previous steps
    # Declare a winner or a draw
    # Option to start a new game

try:
    if __name__ == '__main__':
        board = make_empty_board()
        winner = None
        currentPlayer = None
        currentPlayer = get_players()
        while winner == None:
            # TODO: Show the board to the user.
            print_board(board)

            # TODO: Input a move from the player.
            get_move()

            # TODO: Update the board.

            # TODO: Update who's turn it is.

            # winner = '_'
except:
    print("An error has occurred.")