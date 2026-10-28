employee_1, employee_2, employee_3 = map(int, input().split())

if employee_1 < employee_2 < employee_3:
    res = employee_3 - employee_1
elif employee_2 < employee_1 < employee_3:
    res = employee_3 - employee_2
elif employee_1 < employee_3 < employee_2:
    res = employee_2 - employee_1
elif employee_2 < employee_3 < employee_1:
    res = employee_1 - employee_2
elif employee_3 < employee_2 < employee_1:
    res = employee_1 - employee_3
else:
    res = employee_2 - employee_3

print(res)