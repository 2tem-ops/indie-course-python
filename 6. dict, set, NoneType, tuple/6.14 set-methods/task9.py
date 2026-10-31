s1 = input()
s2 = set(s1)
res = ""

for i in s1:
    if i in s2:
        print(i, end="")
        s2.remove(i)