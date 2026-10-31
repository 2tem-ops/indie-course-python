s = input().lower().split(',')
check = set()

for i in s:
    if i not in check:
        print("НЕТ")
    else:
        print("ДА")
    check.add(i)
