guests = int(input())

if guests % 2 == 0: print(guests // 2)
elif guests % 2 != 0 and guests != 1: print(guests)
else: print(0)