s = input().lower()
print(max(s.count(i) for i in set(s)))