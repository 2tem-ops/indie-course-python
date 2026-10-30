# Сумма строк и столбцов двумерного массива

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

rows, columns = [], []

for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += matrix[i][j]
    rows.append(row_sum)

for j in range(m):
    column_sum = 0
    for i in range(n):
        column_sum += matrix[i][j]
    columns.append(column_sum)

print(*rows)
print(*columns)