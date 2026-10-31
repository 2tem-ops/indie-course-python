# Меняем местами

warehouse = {
    'яблоки': 50,
    'бананы': 30,
    'груши': 70,
    'апельсины': 90
}

print({v: k for k, v in warehouse.items()})
