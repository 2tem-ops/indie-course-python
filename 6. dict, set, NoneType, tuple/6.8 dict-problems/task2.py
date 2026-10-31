s = input().lower()
count = {k: s.count(k) for k in s if k.isalpha()}

print(count)