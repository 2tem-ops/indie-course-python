# Два бандита

a, b = map(int, input().split())

# 4 + 7 = 11
# 11 - 1 = 10 - всего банок
# 10 - 4 = 6
# 10 - 7 = 3

total = a + b - 1
print(total - a, total - b)
