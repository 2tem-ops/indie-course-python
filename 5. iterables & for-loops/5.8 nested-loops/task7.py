# Пузырьковая сортировка

values = [8, 5, 3, 1, 4, 7, 9]
count = 0

for i in range(len(values) - 1):
    for j in range(len(values) - 1 - i):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            count += 1

print(values, count, sep="\n")