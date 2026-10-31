# Ход ферзя

board = [[*input()] for _ in range(8)]
coords = ()

for i, row in enumerate(board):
    for j, col in enumerate(row):
        if col == "F": coords = (i, j)

for i in range(8):
    for j in range(8):
        if board[i][j] != "F":
            if i == coords[0] or j == coords[1]:
                board[i][j] = "+"
            if i - coords[0] == coords[1] - j or i - coords[0] == j - coords[1]:
                board[i][j] = "+"

for row in board:
    print(*row, sep="")
