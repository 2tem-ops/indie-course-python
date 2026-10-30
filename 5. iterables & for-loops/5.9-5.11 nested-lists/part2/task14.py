# Миша и негатив

n, m = map(int, input().split())

matrix_1 = [input() for _ in range(n)]
input()
matrix_2 = [input() for _ in range(n)]

mapping = str.maketrans({"W": "B", "B": "W"})

correct = [row.translate(mapping) for row in matrix_1]
wrong = 0

for i in range(n):
    for j in range(m):
        if matrix_2[i][j] != correct[i][j]:
            wrong += 1

print(wrong)
