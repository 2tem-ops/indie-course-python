# Собираемся в поход

n, count, total = int(input()), 0, 0

while total < n:
    item = int(input())
    if total + item > n:
        break
    total += item
    count += 1


print("Довольно!", n - (n - total), count, sep="\n")

