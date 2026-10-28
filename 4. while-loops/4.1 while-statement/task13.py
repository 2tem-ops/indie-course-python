# Вася и носки

n, m = map(int, input().split())
count = 0
days = 1

while n > 0:
    n -= 1
    if days % m == 0:
        n += 1
    days += 1
    count += 1

print(count)