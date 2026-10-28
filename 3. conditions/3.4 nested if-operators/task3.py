res = ""

if len((s := input())) % 2 == 0:
    res += "четная "
else:
    res += "нечетная "

if len(s) < 6:
    res += "короткая"
else:
    res += "большая"

print(res)