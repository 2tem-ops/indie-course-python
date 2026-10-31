letters = {"a": -10, "b": -20, "c": -5, "d": -15, "e": -1}

print(max(letters, key=lambda i: letters[i]))