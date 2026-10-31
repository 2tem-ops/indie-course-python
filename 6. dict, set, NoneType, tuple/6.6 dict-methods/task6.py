lst = []

for _ in range(int(input())):
    put = input().split()
    john = []
    if len(put) < 2:
        put.append(None)
    if len(put) > 2:
        while len(put) >= 2:
            john.append(put.pop(1))
        put.append(" ".join(john))
    lst.append(put)

print(dict(lst))