matrix = [list(map(int, input().split())) for _ in range(int(input()))]
print(sum(matrix[i][i] for i in range(len(matrix))))