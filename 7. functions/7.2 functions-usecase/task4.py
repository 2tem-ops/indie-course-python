# Инициалы

def print_initials(name: str, surname: str, middlename: str) -> None:
    print(f"{surname.capitalize()} {name[0].upper()}.{middlename[0].upper()}.")
