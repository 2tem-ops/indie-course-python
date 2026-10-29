res = []

for _ in range(int(input())):
    if "соль" not in (s := input()): res.append(s)

print(", ".join(res))