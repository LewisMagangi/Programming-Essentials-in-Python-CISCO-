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

def make_list_of_free_fields(board):
    free_field = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free_field.append(board[i][j])
    return free_field

def enter_move(board):
    value = input("Enter your move: ")
    try:
        value = int(value)
    except:
        print("Please enter an interger !")
        return False
    if value <= 0 or value >= 10:
        print("Please enter an value between 0 and 10 !")
        return False
    elif value not in make_list_of_free_fields(board):
        print("The square is occupied kindly choose another square !")
        return False
    else:
        for i in range(3):
            for j in range(3):
                if value == board[i][j]:
                    board[i][j] = "O"
    return True

def victory_for(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_list = ["X", "X", "X"]
    o_list = ["O", "O", "O"]

    for row in board:
        if row == x_list:
            print("You lost!")
            return True
        elif row == o_list:
            print("You won!")
            return True

    for i in range(3):
        vertical = []
        for j in range(3):
            vertical.append(board[j][i])
        if vertical == x_list:
            print("You lost!")
            return True
        elif vertical == o_list:
            print("You won!")
            return True
    diagonal = []
    for i in range(3):
        diagonal.append(board[i][i])
        if diagonal == x_list:
            print("You lost!")
            return True
        elif diagonal == o_list:
            print("You won!")
            return True

    diagonal = []
    for i in range(3):
        diagonal.append(board[i][2-i])
        if diagonal == x_list:
            print("You lost!")
            return True
        elif diagonal == o_list:
            print("You won!")
            return True

    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        return True

    return False

global Bool 

def draw_move(board):
    from random import randrange
    value = randrange(1, 9)
    if value not in make_list_of_free_fields(board):
        Bool = False 
        return Bool
    elif value in make_list_of_free_fields(board):
        for i in range(3):
            for j in range(3):
                if value == board[i][j]:
                    board[i][j] = "X"
        print(value)
        Bool = True
    return Bool

while not victory_for(board):
    while not enter_move(board):
        enter_move(board)
    display_board(board)
    while Bool is not True:
        draw_move(board)
    display_board(board)
