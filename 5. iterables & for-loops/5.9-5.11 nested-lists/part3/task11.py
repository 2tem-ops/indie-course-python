# Заполнение соседями-2

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in reversed(range(n - 1)):
    for j in reversed(range(m - 1)):
        matrix[i][j] = matrix[i][j + 1] + matrix[i + 1][j]

for row in matrix:
    print(*row)