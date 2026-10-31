lst = list(map(int, input().split()))

print({i: lst.count(i) for i in lst})