words, s1, s2 = input().split(), [], []

for word in words:
    if word.lower() not in s1:
        s1.append(word.lower())
        s2.append(word)

print(" ".join(s2))


