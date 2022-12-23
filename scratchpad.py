import logic
import cli
import tests
import numpy as np

currentPlayer = 'X'

board = logic.make_empty_board()

# board = [
#     [' ', 'X', 'O'],
#     ['X', 'O', 'X'],
#     ['X', 'X', 'O']
# ]



# CHECK WIN CONDITIONS
# https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
# https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/

# def check_rows(sample_win_board):
#     for row in sample_win_board:
#         if len(set(row)) == 1 and row[0] != ' ':
#             return row[0]

# def check_columns(sample_win_board):
#     for col in range(len(sample_win_board[0])):
#         if (
#             (sample_win_board[0][col] != ' ') and
#             (sample_win_board[0][col] == sample_win_board[1][col] == sample_win_board[2][col])
#             ):
#             return sample_win_board[0][col]

# def check_diagonal(sample_win_board):
#     diag_values_top_left = []
#     diag_values_top_right = []
#     for i in range(len(sample_win_board)):
#         diag_values_top_left.append(sample_win_board[i][i])
#     for i in range(len(sample_win_board)):
#         diag_values_top_right.append(
#             sample_win_board[i][len(sample_win_board) - i - 1]
#         )
#     if (
#         (diag_values_top_left[0] != ' ') and
#         (len(set(diag_values_top_left)) == 1)
#         ): 
#         return sample_win_board[0][0]
#     elif (
#         (diag_values_top_right[0] != ' ') and
#         (len(set(diag_values_top_right)) == 1)
#         ):
#         return sample_win_board[0][2]
#     else:
#         return None

# print(check_rows(sample_win_board))
# print(check_columns(sample_win_board))
# print(check_diagonal(sample_win_board))



# logic.get_players()
# if logic.get_players in ('X','O'):
#     currentPlayer = 

# GET MOVE FROM PLAYER:
# def get_move():
#     global board
#     moveRow = int(input("What row would you like to play in?"))
#     moveColumn = int(input("What column would you like to play in?"))
#     if (moveRow < 1 or moveRow > len(board[0])) or (moveColumn < 1 or moveColumn > len(board)):
#         print("Please enter valid positions for row and column.")
#         moveRow = int(input("What row would you like to play in?"))
#         moveColumn = int(input("What column would you like to play in?"))
#     elif board[moveRow - 1][moveColumn - 1] != ' ':
#         print("Please select a different location. The one you requested is already taken.")
#         moveRow = int(input("What row would you like to play in?"))
#         moveColumn = int(input("What column would you like to play in?"))
#     else:
#         board[moveRow - 1][moveColumn - 1] = currentPlayer
#         print("Thank you")

# get_move()
# logic.print_board(board)


# TEST GETTING AND VALIDATING PLAYERS
# def get_players(currentPlayer):
#     first_player = input("Will X or O start?\n")
#     return first_player

# def validate_players(get_players, currentPlayer):
#     if str(get_players(currentPlayer)) != 'X' and str(get_players(currentPlayer)) != 'O':
#         return False
#     else:
#         return True

# print(get_players(currentPlayer))
# validate_players(get_players(currentPlayer))

class PlayerOrder(self, currentPlayer):
    def get_players(currentPlayer):
        first_player = input("Will X or O start?\n")
        return first_player

    def validate_players(get_players, currentPlayer):
        if str(get_players(currentPlayer)) != 'X' and str(get_players(currentPlayer)) != 'O':
            return False
        else:
            return True

currentPlayer = get_players(self, currentPlayer)