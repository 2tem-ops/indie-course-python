# Мишка и старший брат

a, b = map(int, input().split())

count = 0

while a <= b:
    b *= 2
    a *= 3
    count += 1

print(count)