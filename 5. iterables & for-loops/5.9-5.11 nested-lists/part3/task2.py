# Побочная диагональ

matrix = [list(map(int, input().split())) for _ in range(int(input()))]
print(max(matrix[i][len(matrix) - i - 1] for i in range(len(matrix))))