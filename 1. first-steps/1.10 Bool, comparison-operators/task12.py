a, b, c = map(int, input().split())

hypotenuse = max(a, b , c)
cathetus_1 = min(a, b , c)
cathetus_2 = a + b + c - min(a, b, c) - max(a, b, c)

print(cathetus_1 ** 2 + cathetus_2 ** 2 == hypotenuse ** 2)

