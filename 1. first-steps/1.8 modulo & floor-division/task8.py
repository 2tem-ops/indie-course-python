# Выиграть в лотерею

n = int(input())

# print(n // 100)
# print(n % 100 // 20)
# print(n % 20 // 10)
# print(n % 10 // 5)
# print(n % 5 // 1)
print(n // 100 + n % 100 // 20 + n % 20 // 10 + n % 10 // 5 + n % 5 // 1)