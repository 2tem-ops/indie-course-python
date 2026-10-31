# Фильтрация книг

books = {
    'ASDFG': 320,
    'ZXC123': 250,
    'QWE': 110,
    'MNBVCXZ': 410,
    'LKH': 90
}

print({k: v for k, v in books.items() if len(k) % 3 == 0})