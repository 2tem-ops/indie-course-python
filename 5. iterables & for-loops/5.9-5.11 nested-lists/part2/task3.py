# Обход элементов матрицы - 3

n, m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n -1, -1, -1):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()
