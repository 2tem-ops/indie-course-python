# Продолжение "Буквенного детектива"

letters = {'к': [0, 4], 'о': [1], 'т': [2], 'и': [3]}

word_length = sum([len(value) for value in list(letters.values())])
word = ["X"] * word_length

for key, value in letters.items():
    for i in value:
        word[i] = key

print("".join(word))