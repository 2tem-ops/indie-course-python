n, i, total = int(input()), 1, set()

while i ** 2 <= n:
    if n % i == 0:
        total.add(i)
        if i != n // i:
            total.add(n // i)
    i += 1

print(sum(total))