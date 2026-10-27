print("""Для числа {nn} предыдущим будет число {n}. 
Для числа {nn} следующим будет число {nnn}.
""".format(nn = (nn := input()), n = int(nn) - 1, nnn = int(nn) + 1))