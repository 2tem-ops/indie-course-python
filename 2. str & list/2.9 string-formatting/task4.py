course_1, course_2, course_3 = float(input()), float(input()), float(input())

print("Средний курс доллара за последние три дня: %.2f RUB." % (round((course_1 + course_2 + course_3) / 3, 2)))