# Система регистрации

n = int(input())
database = {}

for _ in range(n):
    entry = input()
    if entry not in database:
        database.setdefault(entry, 1)
        print("OK")
    else:
        print(entry + str(database[entry]))
        database[entry] += 1