EMPTY = "-"
ROOK = "ROOK"
board = []
break_loop = True

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

for i in range(8):
    for j in range(8):
        if board[i][j] == "-":
            answer = input("Do you want to fill the board with a piece ?, Type : Yes or No :")
            if answer == "No":
                print("Great nice time !")
                break
            elif answer == "Yes":
                board[i][j] = input("Kindly enter a valid chess piece to be inputed :")
                print("The ", board[i][j], "has been entered successfully !")
            else:
                print("That/'s not a valid choice, Kindly enter a choice again")
print(board)
