# Поиск лидеров

scores = {
    'Анна': (100, 1.0),
    'Ольга': (120, 0.8),
    'Геракл': (100, 1.2),
    'Игорь': (80, 1.5)
}

best = []

max_value = max(scores.values(), key=lambda i: i[0] * i[1])
max_value = max_value[0] * max_value[1]

for employee, score in scores.items():
    if score[0] * score[1] == max_value:
        best.append(employee)

print(best[0] if len(best) == 1 else best)