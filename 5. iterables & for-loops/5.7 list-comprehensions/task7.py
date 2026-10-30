a, b = map(int, input().split())

print([i ** 2 if a <= b else (a + b - i) ** 3 for i in range(min(a, b), max(a, b) + 1)])