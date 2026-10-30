values = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum([element for sublist in values for element in sublist if element % 2 == 0]))