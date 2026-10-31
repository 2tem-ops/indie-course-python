# Реверсивные пары

strings = ["hello", "world", "madam", "python"]
print([word if word == word[::-1] else (word, word[::-1]) for word in strings])

