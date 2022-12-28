# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable

# new_board = [
#             [' ',' ',' '],
#             [' ',' ',' '],
#             [' ',' ',' ']
#             ]

class Board:
    def __init__(self):
        self.grid = None

    def new_board(self):
        self.grid = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
            ]

    def print_board(self):
        print('-' + '-' + '1' + '-' + '-' + '-' + '2' + '-' + '-' + '-' + '3' + '-')
        print('1 '+ self.grid[0][0] + ' | ' + self.grid[0][1] + ' | ' + self.grid[0][2])
        print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
        print('2 '+ self.grid[1][0] + ' | ' + self.grid[1][1] + ' | ' + self.grid[1][2])
        print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
        print('3 '+ self.grid[2][0] + ' | ' + self.grid[2][1] + ' | ' + self.grid[2][2])

class Players:
    def __init__(self):
        self.first_player = None
        self.second_player = None

    def first_player_selection(self):
        self.first_player = input("Will 'X' or 'O' start?")
        return self.first_player

    def validate_player_selection(self):
        if self.first_player != 'X' and self.first_player != 'O':
            return False
        else:
            return True

    def get_first_player(self):
        self.first_player_selection()
        if self.validate_player_selection():
            return self.first_player
        else:
            while self.validate_player_selection() == False:
                print("Please make a valid selection of either 'X' or 'O'.")
                self.first_player_selection()

    def get_second_player(self):
        if self.first_player == 'X':
            self.second_player = 'O'
            return self.second_player
        else:
            self.second_player = 'X'
            return self.second_player

    def get_first_player_name(self):
        self.first_player_name = input("Please enter the name of the first player.")
        if self.first_player_name:
            return self.first_player_name
        else:
            while self.first_player_name == '':
                print("Please enter a non-empty response.")
                self.first_player_name = input("Please enter the name of the first player.")

    def get_second_player_name(self):
        self.second_player_name = input("Please enter the name of the second player.")
        if self.second_player_name:
            return self.second_player_name
        else:
            while self.second_player_name == '':
                print("Please enter a non-empty response.")
                self.second_player_name = input("Please enter the name of the second player.")


class Moves:
    def __init__(self):
        self.move_row = None
        self.move_column = None
    
    def get_move(self):
        while True:
            try:
                self.move_row = int(input("What row would you like to play in?"))
                self.move_column = int(input("What column would you like to play in?"))
            except ValueError:
                print("Please enter an integer value for row and column.")
                #Return to the start of the loop
                continue
            else:
                #Exit the loop
                break

    def validate_move(self, grid):
        """
        This function returns a boolean to indicate whether the move is valid or not
        as well as the reason for any error if the boolean returns False. 
        """
        if (self.move_row < 1 or self.move_row > len(grid[0])) or (self.move_column < 1 or self.move_column > len(grid)):
            self.is_valid = False
            self.error_message = "B"
            return self.is_valid, self.error_message
        elif grid[self.move_row - 1][self.move_column - 1] != ' ':
            self.is_valid = False
            self.error_message = "T"
            return self.is_valid, self.error_message
        elif grid[self.move_row - 1][self.move_column - 1] == ' ':
            self.is_valid = True
            self.error_message = None
            return self.is_valid, self.error_message
        else:
            self.is_valid = False
            self.error_message = None
            return self.is_valid, self.error_message

    def execute_move(self, grid, current_player):
        while self.is_valid == False:
            self.get_move()
            self.validate_move(grid)
            if self.error_message == 'T':
                print("Please select a different location. The one you requested is already taken.")
                continue
            elif self.error_message == 'B':
                print(f"Please enter positions for row and column that fit the game boundaries: {len(grid[0])} x {len(grid)}.")
                continue
        if self.is_valid:
            grid[self.move_row - 1][self.move_column - 1] = current_player

class GameRules:
    def __init__(self):
        self.diag_values_top_left = []
        self.diag_values_top_right = []
        self.winning_symbol = None
        self.winner = False

    # Game winning conditions
    def check_rows(self, board):
        for row in board:
            if len(set(row)) == 1 and row[0] != ' ':
                self.winning_symbol = row[0]
                self.winner = True
                return self.winning_symbol, self.winner

    def check_columns(self, board):
        for col in range(len(board[0])):
            if (
                (board[0][col] != ' ') and
                (board[0][col] == board[1][col] == board[2][col])
                ):
                self.winning_symbol = board[0][col]
                self.winner = True
                return self.winning_symbol, self.winner

    def check_diagonal(self, board):
        for i in range(len(board)):
            self.diag_values_top_left.append(board[i][i])
        for i in range(len(board)):
            self.diag_values_top_right.append(
                board[i][len(board) - i - 1]
            )
        if (
            (self.diag_values_top_left[0] != ' ') and
            (len(set(self.diag_values_top_left)) == 1)
            ):
            self.winning_symbol = board[0][0]
            self.winner = True
            return self.winning_symbol, self.winner
        elif (
            (self.diag_values_top_right[0] != ' ') and
            (len(set(self.diag_values_top_right)) == 1)
            ):
            self.winning_symbol = board[0][2]
        else:
            return None

    # def check_for_win(self, board):
    #     while self.winner == False:
    #         for row in board:
    #             if len(set(row)) == 1 and row[0] != ' ':
    #                 self.winning_symbol = row[0]
    #                 self.winner = True
    #                 return self.winning_symbol, self.winner
    #                 break
    #             else:

        
    # End game winning conditions

    def advance_turn(self, current_player):
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    
    def board_full(self, board):
        for row in board:
            for position in row:
                if position == ' ':
                    return False
        return True

# class GameSetup:
#     def __init__(self):
#         players = Players()
#         players.first_player = 

class RunGame:
    def __init__(self):
        self.players = Players()
        self.first_player = self.players.get_first_player()
        self.first_player_name = self.players.get_first_player_name()
        self.second_player = self.players.get_second_player()
        self.second_player_name = self.players.get_second_player_name()
        self.gameboard = Board()
        self.board = self.gameboard.new_board()
        self.gameboard.print_board()
        # print(f"First player is {self.first_player} and second player is {self.second_player}.")
        self.gamerules = GameRules()

    def gameplay(self):
        win_condition = self.gamerules.check_rows(self.gameboard)
        print(win_condition)