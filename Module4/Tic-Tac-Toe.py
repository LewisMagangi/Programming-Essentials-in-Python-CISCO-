board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9],
] 

def display_board(board):
    def first_line (board):
        print("+-------+-------+-------+")
    def second_line (board):
        print("|       |       |       |")
    def blank_line (board):
        print("                         ")
    first_line(board)
    blank_line(board)
    second_line(board)
    blank_line(board)
    print("|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |")
    blank_line(board)
    second_line(board)
    blank_line(board)
    first_line(board)
    blank_line(board)
    second_line(board)
    blank_line(board)
    print("|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |")
    blank_line(board)
    second_line(board)
    blank_line(board)
    first_line(board)
    blank_line(board)
    second_line(board)
    blank_line(board)
    print("|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |")
    blank_line(board)
    second_line(board)
    blank_line(board)
    first_line(board)
    """The function accepts one parameter containing the board's current status
       and prints it out to the console."""

def enter_move(board):
    value = int(input("Enter your move: "))
    for i in range(3):
        for j in range(3):
            if value == board[i][j]:
                board[i][j] = "O"
        
    """The function accepts the board's current status, asks the user about their move, 
       checks the input, and updates the board according to the user's decision."""

def make_list_of_free_fields(board):
    free_field = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free_field.append(board[i][j])
                    
    """The function browses the board and builds a list of all the free squares; 
       the list consists of tuples, while each tuple is a pair of row and column numbers."""

def victory_for(board, sign):
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("You won!")
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("You won!")
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
         print("You won!")
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
         print("You won!")
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
         print("You won!")
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
         print("You won!")
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
         print("You won!")
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
         print("You won!")
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("You lost!")
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("You lost!")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
         print("You lost!")
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
         print("You lost!")
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
         print("You lost!")
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
         print("You lost!")
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
         print("You lost!")
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
         print("You lost!")
         
    
    """The function analyzes the board's status in order to check if 
       the player using 'O's or 'X's has won the game"""

def draw_move(board):
    from random import randrange
    value = randrange(1, 9)
     for i in range(3):
        for j in range(3):
            if value == board[i][j]:
                board[i][j] = "X"

    """The function draws the computer's move and updates the board."""

