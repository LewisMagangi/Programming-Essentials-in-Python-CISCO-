board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, "O", 9],
] 

def make_list_of_free_fields(board):
    free_field = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free_field.append(board[i][j])
    print(free_field)

make_list_of_free_fields(board)
