# Электронные часы - 2

n = int(input())

hours = n // 3600
minutes = (n // 60) % 60
seconds = n % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")