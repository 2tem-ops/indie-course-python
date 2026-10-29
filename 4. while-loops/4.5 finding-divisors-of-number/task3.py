n, i, is_prime = int(input()), 2, True

if n == 1: is_prime = False

while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

print("Yes" if is_prime else "No")
