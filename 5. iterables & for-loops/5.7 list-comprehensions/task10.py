from string import ascii_uppercase

n = int(input())
print([i * (ascii_uppercase.index(i) + 1) for i in ascii_uppercase[:n]])