# A. Красивая матрица

matrix = [list(map(int, input().split())) for _ in range(5)]

res = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            if i > 2 and j <= 2:
                res = i - j
            elif i < 2 and j > 2:
                res = j - i
            elif i == 2 and j < 2:
                res = (2 + 2) - (i + j)
            elif i < 2 and j == 2:
                res = abs(i - 2)
            elif i > 2 and j > 2:
                res = abs((i + j) - (2 + 2))
            elif i == j:
                res = abs((i + j) - (2 + 2))

print(res)