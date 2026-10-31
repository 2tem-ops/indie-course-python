# A. Матчи

matrix = [list(map(int, input().split())) for _ in range(int(input()))]
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
         if matrix[i][0] == matrix[j][1]:
            count += 1

print(count)

