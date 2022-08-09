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
    value = input("Enter your move: ")

    try:
        value = int(value)
    except:
        print("The input must be an interger !")
        return False
    if value <= 0 or value >= 10:
        print("Please enter a value between 0 and 10 !")
    elif value not in make_list_of_free_fields
        
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
