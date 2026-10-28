# Зимний вечер в Бурсе

n = int(input())
while str(n)[0] != "1" and n < 1_000_000_000: n *= int(str(n)[0])
print(n)