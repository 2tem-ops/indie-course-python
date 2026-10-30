# Обход элементов матрицы - 4

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m - 1, -1, -1):
        print(matrix[i][j], end=" ")
    print()