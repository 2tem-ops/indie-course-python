# Избавляемся от слабых звеньев

scores = {
    'Иванов': 15,
    'Петров': 20,
    'Сидоров': 15,
    'Кузнецов': 25
}

print({k: v for k, v in scores.items() if v != min(scores.values())})