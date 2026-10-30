# Обход элементов матрицы - 1

matrix = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[j][i], end=" ")
    print()