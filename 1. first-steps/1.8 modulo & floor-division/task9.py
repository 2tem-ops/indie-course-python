# Следующее четное

n = int(input())

# print((n - n // 2) * 2)
#
# print(n + (n // (n // 2)))

print(n + (n + (n // (n // 2))) - ((n - n // 2) * 2))