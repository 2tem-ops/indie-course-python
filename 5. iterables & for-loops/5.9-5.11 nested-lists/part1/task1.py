values = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

print(sum(len(sublist) for sublist in values), len([sublist for sublist in values if sublist]), sep="\n")