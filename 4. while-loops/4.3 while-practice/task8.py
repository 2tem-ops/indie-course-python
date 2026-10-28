# Три удара и в блок

password, limit = input(), 3

while limit > 0:
    if input() != password:
        limit -= 1
        print("Введен неправильный пароль!", f"Лимит попыток = {limit}", sep="\n")
    else:
        print("Вы ввели правильный пароль! Добро пожаловать!")
        break
else:
    print("Вы потратили все свои попытки! Приходите завтра")