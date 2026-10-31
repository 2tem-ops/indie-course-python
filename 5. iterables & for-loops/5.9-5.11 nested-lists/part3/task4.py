# Ход ладьи

board = [[*input()] for _ in range(8)]
coords = ()

for i in range(8):
    for j in range(8):
        if board[i][j] == "T":
            coords = (i, j)
            break
    if coords:
        break

for i in range(8):
    for j in range(8):
        if i == coords[0]:
            if board[i][j] != "T": board[i][j] = "+"
        if j == coords[1]:
            if board[i][j] != "T": board[i][j] = "+"

for row in board:
    print(*row, sep="")