def count_letters(text: str) -> None:
    uppercase = sum(i.isupper() for i in text)
    lowercase = sum(i.islower() for i in text)
    print(f"Количество заглавных символов: {uppercase}")
    print(f"Количество строчных символов: {lowercase}")