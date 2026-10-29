n, maximum, minimum = int(input()), 0, 9

while n > 0:
    if n % 10 > maximum: maximum = n % 10
    if n % 10 < minimum: minimum = n % 10
    n //= 10

print(minimum, maximum, sep="\n")