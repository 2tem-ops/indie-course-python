# Ваня и кубики

k = int(input())
total, row, count = 1, 1, 1

while total < k:
    row += 1
    count += row
    total += count

if total > k:
    row -= 1

print(row)