# Треугольник Паскаля

n = int(input())
pascal = [[1 if i == j or i == 0 else 0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        pascal[i][j] = pascal[i - 1][j] + pascal[i - 1][j - 1]

for i in range(0, n + 1):
    for j in range(0, i + 1):
        print(pascal[i][j], end=" ")
    print()