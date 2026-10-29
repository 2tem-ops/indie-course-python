# Линейный поиск

s, target = map(int, input().split()), int(input())

for i, v in enumerate(s, start=1):
    if v == target: print(i); break
else: print("ErrorValue")