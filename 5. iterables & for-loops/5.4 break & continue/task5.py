messages = ["Заказ отправлен", "Ожидается доставка", "Товар в пути"]
substring = "доставка"

for msg in messages:
    if substring.lower() in msg.lower(): print(msg); break
else: print("Подстрока не найдена")
