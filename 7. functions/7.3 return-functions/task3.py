def fizz_buzz(n: int) -> str | int:
    res = ""
    if n % 3 == 0:
        res += "Fizz"
    if n % 5 == 0:
        res += "Buzz"
    return res if res else n

def generate_fizz_buzz_list(n: int) -> list[int | str]:
    res = [fizz_buzz(i) for i in range(1, n + 1)]
    return res

print(generate_fizz_buzz_list(30))