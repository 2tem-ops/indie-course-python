check = [i for i in map(int, input().split()) if i > 0]
print("Empty" if not check else min(check))