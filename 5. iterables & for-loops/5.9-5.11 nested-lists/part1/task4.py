values = [
    [5, 2, 8],
    [1, 6, 3],
    [7, 4, 9]
]

print(min(min(sublist) for sublist in values if sublist) if values else "Список пуст")