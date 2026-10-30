matrix = [input() for _ in range(4)]
flag = True

for i in range(3):
    for j in range(3):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            flag = False
            break
    if not flag:
        break

print("Yes" if flag else "No")