# Состязания - 2

rows, columns = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
maximum = [(elem, matrix.index(row), row.index(elem)) for row in matrix for elem in row]
print((res := max(maximum, key=lambda x: x[0]))[0])
print(res[1], res[2])