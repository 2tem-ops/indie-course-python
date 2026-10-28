s, index = input(), 0

while index < len(s):
    if s[index] in "ea":
        print("Ага! Нашлась")
        break

    print(f"Текущая буква: {s[index]}")
    index += 1
else:
    print("Распечатали все буквы")
