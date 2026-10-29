words = ["apple", "banana", "cherry", "strawberry", "kiwi", "mango", "blueberry"]

print(*[word for word in words if len(word) > 6], sep="\n")