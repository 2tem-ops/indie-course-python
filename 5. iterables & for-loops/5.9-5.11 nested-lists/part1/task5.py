# Преобразование одномерного списка в двумерный

n, lst = int(input()), list(map(int, input().split()))
k, r = map(int, input().split())

res = []

while lst:
    data = lst[:r]
    del lst[:r]
    res.append(data)

print(res)