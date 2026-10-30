# Состязания - 3

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

winner = max(range(n), key=lambda i: (max(matrix[i]), sum(matrix[i]), -i))
print(winner)