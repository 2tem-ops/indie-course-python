# Постулат Бертрана

n = int(input())
count = 0

for i in range(n + 1, n * 2):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        count += 1

print(count)