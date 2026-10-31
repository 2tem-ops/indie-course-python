# Заполнение матрицы

n = int(input())
A, B, C = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = C
        elif i < j:
            matrix[i][j] = A
        else:
            matrix[i][j] = B

for row in matrix: print(*row)