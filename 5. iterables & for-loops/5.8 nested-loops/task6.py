# Кодовое слово с цифрой

messages = ["Просто текст", "Ещё немного текста", "Совершенно ничего лишнего"]
found = False

for msg in messages:
    if not found:
        if any(char.isdigit() for char in msg):
            for word in msg.split():
                if any(char.isdigit() for char in word):
                    print(word)
                    found = True
                    break
        if found:
            break
else:
    print("Кодовое слово не найдено")