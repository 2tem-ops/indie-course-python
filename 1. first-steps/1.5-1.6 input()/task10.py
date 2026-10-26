# Разность времен

h1, m1, s1 = int(input()), int(input()), int(input())
h2, m2, s2 = int(input()), int(input()), int(input())

s1 = s1 + h1 * 60 * 60 + m1 * 60
s2 = s2 + h2 * 60 * 60 + m2 * 60

print(s2 - s1)