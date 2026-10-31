# Учёт гласных

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

s = input().lower()
print({vowel: s.count(vowel) for vowel in vowels if s.count(vowel) != 0})
