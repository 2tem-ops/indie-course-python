income, desired, total = list(map(int, input().split())), int(input()), 0

while income and total < desired: total += income.pop(0)

print(total, ["Цель не достигнута", "Цель достигнута"][total >= desired], sep="\n")

