# Счастливый билет

a = f"{int(input()):06d}"
print("YES" if sum(map(int, a[0:3])) == sum(map(int, a[-3:])) else "NO")