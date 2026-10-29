a, b = map(int, input().split())
first, second = a, b

while b:
    a, b = b, a % b

print(first * second // a)