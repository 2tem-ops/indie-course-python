events = {
    'Выставка': ['Ольга', 'Сергей'],
    'Семинар': ['Сергей', 'Игорь'],
    'Тренинг': ['Ольга', 'Дарья']
}

database = {}

for event, persons in events.items():
    for person in persons:
        database.setdefault(person, []).append(event)

print(database)