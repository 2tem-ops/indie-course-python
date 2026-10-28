move_1, move_2 = input(), input()

print("YES" if ((ord(move_1[0]) + int(move_1[1])) + (ord(move_2[0]) + int(move_2[1]))) % 2 == 0 else "NO")
