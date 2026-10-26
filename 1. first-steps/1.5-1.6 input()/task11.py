# Выражение

a, b, c = int(input()), int(input()), int(input())

opp1 = a + b + c
opp2 = a * (b + c)
opp3 = a * b * c
opp4 = (a + b) * c
opp5 = (a + c) * b
opp6 = (b + c) * a

print(max(opp1, opp2, opp3, opp4, opp5, opp6))