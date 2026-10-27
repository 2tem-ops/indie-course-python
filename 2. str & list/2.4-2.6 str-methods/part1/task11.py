# Упражнение на строки

s = input()
s = s.lower().replace("a", "").replace("o", "").replace("y", "").replace("u", "").replace("e", "").replace("i", "")
print(s.replace("", ".").rstrip("."))
