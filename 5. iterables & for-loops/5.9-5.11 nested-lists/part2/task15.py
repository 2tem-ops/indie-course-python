# A. Таблица умножения

n, x = list(map(int, input().split()))
matrix = [[0] * n for _ in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        matrix[i][j] = (i + 1) * (j + 1)

for row in matrix:
    for elem in row:
        if elem == x: count += 1
        #print(f"{str(elem).zfill(2):^2}", end=" ")
    #print()

print(count)