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
display_board(board)
