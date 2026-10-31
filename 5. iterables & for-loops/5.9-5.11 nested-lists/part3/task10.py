# Заполнение соседями

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

for row in matrix:
    print(*row)