# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable

board = None
runGame = True
currentPlayer = None
winner = None

# def make_empty_board(self):
def make_empty_board():
    return [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

def reset_board(make_empty_board):
    board = make_empty_board()

def get_players(self, currentPlayer):
    first_player = input("Will X or O start?\n")
    return first_player

# Review for ERROR:
def validate_players(self, get_players):
    if self.get_players(currentPlayer) != 'X' and self.get_players(currentPlayer) != 'O':
        return False
    else:
        return True

# Check win conditions:
def check_rows(board):
    global winner
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            # return row[0]
            winner = row[0]

def check_columns(board):
    global winner
    for col in range(len(board[0])):
        if (
            (board[0][col] != ' ') and
            (board[0][col] == board[1][col] == board[2][col])
            ):
            # return board[0][col]
            winner = board[0][col]

def check_diagonal(board):
    global winner
    diag_values_top_left = []
    diag_values_top_right = []
    for i in range(len(board)):
        diag_values_top_left.append(board[i][i])
    for i in range(len(board)):
        diag_values_top_right.append(
            board[i][len(board) - i - 1]
        )
    if (
        (diag_values_top_left[0] != ' ') and
        (len(set(diag_values_top_left)) == 1)
        ): 
        # return board[0][0]
        winner = board[0][0]
    elif (
        (diag_values_top_right[0] != ' ') and
        (len(set(diag_values_top_right)) == 1)
        ):
        # return board[0][2]
        winner = board[0][2]
    else:
        return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'O' # FIXME

def get_move(board):
    # global board
    moveRow = int(input("What row would you like to play in?"))
    moveColumn = int(input("What column would you like to play in?"))
    if (moveRow < 1 or moveRow > len(board[0])) or (moveColumn < 1 or moveColumn > len(board)):
        print("Please enter valid positions for row and column.")
        moveRow = int(input("What row would you like to play in?"))
        moveColumn = int(input("What column would you like to play in?"))
    elif board[moveRow - 1][moveColumn - 1] != ' ':
        print("Please select a different location. The one you requested is already taken.")
        moveRow = int(input("What row would you like to play in?"))
        moveColumn = int(input("What column would you like to play in?"))
    else:
        board[moveRow - 1][moveColumn - 1] = currentPlayer
        print("Thank you")

# def validate_move(board)

def assign_move_value(get_move):
    board[get_move[0]][get_move[1]] = currentPlayer

def print_board(board):
    print('-' + '-' + '1' + '-' + '-' + '-' + '2' + '-' + '-' + '-' + '3' + '-')
    print('1 '+ board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
    print('2 '+ board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
    print('3 '+ board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])