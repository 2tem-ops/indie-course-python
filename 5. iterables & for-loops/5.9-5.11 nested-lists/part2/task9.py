# Состязания

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
maximum = [sum(row) for row in matrix]
print(max(maximum), maximum.index(max(maximum)), sep="\n")