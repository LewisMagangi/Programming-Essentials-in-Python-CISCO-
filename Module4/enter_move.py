board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9],
]


def make_list_of_free_fields(board):
    free_field = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free_field.append(board[i][j])
    return free_field

def enter_move(board, free_field):
    try:
        value = int(input("Enter your move: "))
    except ValueError:
        print("Please enter an interger !")
    try:
        if value <= 0 or value >= 10:
            print("Please enter a value in the range 1 to 9 !")
    except UnboundLocalError:
        print("The value entered is not applicable !")
    make_list_of_free_fields(board)
    if value in free_field:
        for i in range(3):
            for j in range(3):
                if value == board[i][j]:
                    board[i][j] = "O"
    else:
        print("The square is occupied, Kindly choose another square !")
    return board
make_list_of_free_fields(board)
enter_move(board, free_field)
print(board, free_field)
