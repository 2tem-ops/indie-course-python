n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
a = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = i * m + j
    else:
        for j in range(m):
            matrix[i][j] = i * m + m - (j + 1)


for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]:<2}", end=' ')
    print()