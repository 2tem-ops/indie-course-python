# Воронеж! Тебе на «Ж»

city_1, city_2 = input().lower(), input().lower()

if city_1.endswith("ь"):
    res = "Good" if city_1[-2] == city_2[0] else "Bad"
else:
    res = "Good" if city_1[-1] == city_2[0] else "Bad"

print(res)
