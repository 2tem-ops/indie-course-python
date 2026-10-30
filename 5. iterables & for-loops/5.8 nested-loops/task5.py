# Система уравнений

n, m = map(int, input().split())
count = 0

for a in range(1001):
    for b in range(1001):
        if a == m - b ** 2 and b == n - a ** 2:
            count += 1

print(count)