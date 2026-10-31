# Буквенный детектив

res = {}

for index, ltr in enumerate(input()):
    res.setdefault(ltr, []).append(index)

print(res)