board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9],
]

def enter_move(board):
    try:
        value = int(input("Enter your move: "))
    except ValueError:
        print("Please enter an interger !")
    try:
        if value <= 0 or value >= 10:
            print("Please enter a value in the range 1 to 9 !")
    except UnboundLocalError:
        print("The value entered is not applicable !")
    else:
        for i in range(3):
            for j in range(3):
                if value == board[i][j]:
                    board[i][j] = "O"
    return board
enter_move(board)
print(board)
