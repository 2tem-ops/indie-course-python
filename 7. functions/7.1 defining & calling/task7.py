def check_password(password: str) -> None:
    nums, upper, symbol, length = 0, False, False, len(password)
    for char in password:
        if char.isdigit():
            nums += 1
        if char in "!@#$%*":
            symbol = True
        if char.isupper():
            upper = True
    print("Perfect password" if nums >= 3 and upper and symbol and length >= 10 else "Easy peasy")