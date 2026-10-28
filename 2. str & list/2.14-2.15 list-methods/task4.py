# Метод pop

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]

total = 0

total += numbers.pop()
total += numbers.pop(0)
total += numbers.pop(12)
total += numbers.pop(7)

print(numbers, total, sep="\n")