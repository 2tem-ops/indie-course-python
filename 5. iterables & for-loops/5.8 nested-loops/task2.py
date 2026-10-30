# Шахматная доска

n = int(input())

for i in range(n):
    for j in range(n):
        print("X" if (i + j) % 2 == 0 else "O", end=" ")
    print()