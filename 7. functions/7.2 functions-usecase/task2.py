def is_between(a: int, b: int, c:int) -> None:
    print(True if min(b, c) <= a <= max(b, c) else False)

is_between(5, 9, 1)