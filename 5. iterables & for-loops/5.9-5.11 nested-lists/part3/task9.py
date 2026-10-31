# Ход коня

board = [[*input()] for _ in range(8)]
coords = ()

for i, row in enumerate(board):
    for j, col in enumerate(row):
        if col == "H": coords = (i, j)

for i in range(8):
    for j in range(8):
        if board[i][j] != "H":
            i1, j2 = abs(i - coords[0]), abs(j - coords[1])
            if i1 * j2 == 2:
                board[i][j] = "+"

for row in board:
    print(*row, sep="")