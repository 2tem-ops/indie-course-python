# Кратные 3 или 5

total = 0
for num in range(1, int(input())):
    if num % 3 == 0 or num % 5 == 0: total += num

print(total)