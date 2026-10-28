# Новый год и спешка

n, k = map(int, input().split())
count, time = 1, 0

while n > 0:
    if k + (time + 5 * count) > 240:
        break
    time += 5 * count
    n -= 1
    count += 1

print(count - 1)

