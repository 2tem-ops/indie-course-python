# Морской бой - 2

n, m = map(int, input().split())
board = []

for i in range(n):
    board.append("." + input() + ".")

board.insert(0, "." * (m + 2))
board.append("." * (m + 2))

count = 0

for i in range(1, n + 1):
    if "." in board[i]:
        for j in range(1, m + 1):
            dot = board[i][j]
            if dot == ".":
                if dot == board[i + 1][j] and dot == board[i - 1][j] and dot == board[i][j + 1] and dot == board[i][j - 1]:
                    count += 1

print(count)