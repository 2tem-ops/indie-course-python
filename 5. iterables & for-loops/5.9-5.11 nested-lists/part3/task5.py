# Ход слона

board = [[*input()] for _ in range(8)]
coords = ()

for i, row in enumerate(board):
    for j, col in enumerate(row):
        if col == "S": coords = (i, j)

for i in range(8):
    for j in range(8):
        if (i - coords[0] == j - coords[1]) or (coords[0] - i == j - coords[1]):
            if board[i][j] != "S": board[i][j] = "+"

for row in board:
    print(*row, sep="")