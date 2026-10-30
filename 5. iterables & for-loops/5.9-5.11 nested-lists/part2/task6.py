# Матрица из семёрок

n, m = map(int, input().split())

print(matrix := [[7] * m for _ in range(n)])
for row in matrix: print(*row)