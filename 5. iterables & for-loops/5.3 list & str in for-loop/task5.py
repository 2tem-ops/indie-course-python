ltr, s = input(), input().split()

print("\n".join(i for i in s if ltr.lower() in i.lower()))