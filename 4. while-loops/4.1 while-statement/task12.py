x, y = map(int, input().split())
count = 1

while x < y:
    x = x * 1.15
    count += 1

print(count)