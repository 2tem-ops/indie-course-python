values = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
n = 0

[(sublist.insert(0, n), sublist.append(n)) for sublist in values]

print(values)