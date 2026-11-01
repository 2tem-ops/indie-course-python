words = ["Python", "мы любим", "тебя"]
for index in range(5):
    try:
        print(index, words[index])
    except IndexError:
        print(f"Индекс {index} вышел за границы списка")
        break
print('Знай это')
