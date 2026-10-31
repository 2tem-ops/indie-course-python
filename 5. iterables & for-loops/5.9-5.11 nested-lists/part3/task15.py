# A. Тортминатор

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
columns = []

for j in range(m):
    lst = []
    for i in range(n):
        lst.append(matrix[i][j])
    columns.append("".join(lst))

x, y = 0, 0

for row in matrix:
    if "S" not in row:
        x += 1

for col in columns:
    if "S" not in col:
        y += 1

print(x * m + y * (n - x))

# print(matrix)
# print(columns)
