# Симметричная ли матрица?

matrix = [list(map(int, input().split())) for _ in range(int(input()))]
symmetrical = True


for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i != j:
            if matrix[i][j] != matrix[j][i]:
                symmetrical = False
                break

    if not symmetrical:
        break

print("Yes" if symmetrical else "No")