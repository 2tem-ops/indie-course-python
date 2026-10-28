# Бал в БерлГУ

n, boys = int(input()), sorted(list(map(int, input().split())))
m, girls = int(input()), sorted(list(map(int, input().split())))

i, j, count = 0, 0, 0

while i < len(boys) and j < len(girls):
    if abs(boys[i] - girls[j]) <= 1:
        i += 1
        j += 1
        count += 1
    else:
        if boys[i] < girls[j]:
            i += 1
        else:
            j += 1

print(count)
