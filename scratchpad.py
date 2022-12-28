class Board:
    def __init__(self):
        self.grid = None

    def new_board(self):
        self.grid = [
            [' ',' ',' '],
            [' ','X',' '],
            [' ',' ',' ']
            ]

    def print_board(self):
        print('-' + '-' + '1' + '-' + '-' + '-' + '2' + '-' + '-' + '-' + '3' + '-')
        print('1 '+ self.grid[0][0] + ' | ' + self.grid[0][1] + ' | ' + self.grid[0][2])
        print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
        print('2 '+ self.grid[1][0] + ' | ' + self.grid[1][1] + ' | ' + self.grid[1][2])
        print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
        print('3 '+ self.grid[2][0] + ' | ' + self.grid[2][1] + ' | ' + self.grid[2][2])

class Moves:
    def __init__(self):
        self.move_row = None
        self.move_column = None
        self.is_valid = False
    
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
        
    # def get_move(self):
    #     self.move_row = int(input("What row would you like to play in?"))
    #     self.move_column = int(input("What column would you like to play in?"))

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

    def execute_move(self, grid):
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
            grid[self.move_row - 1][self.move_column - 1] = 'X'

        # if self.is_valid:
        #     grid[self.move_row - 1][self.move_column - 1] = 'X'
        # else:
        #     while self.is_valid == False:
        #         if self.error_message == 'T':
        #             print("Please select a different location. The one you requested is already taken.")
        #         elif self.error_message == 'B':
        #             print(f"Please enter positions for row and column that fit the game boundaries \
        #                 ({len(grid[0])} x {len(grid)}).")
                

board = Board()
board.new_board()
board.print_board()
a = Moves()
a.execute_move(board.grid)
board.print_board()