def draw_move():
    from random import randrange
    value = randrange(1, 9)
    for i in range(3):
        for j in range(3):
            if value == board[i][j]:
                board[i][j] = "X"
