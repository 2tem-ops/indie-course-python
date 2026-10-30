# Состязания - 4

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_elem = max(elem for row in matrix for elem in row)
print(len(set([tuple(row) for row in matrix for elem in row if elem == max_elem])))