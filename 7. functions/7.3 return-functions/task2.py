def factorial(n: int) -> int:
    pr = 1
    for i in range(2, n + 1):
        pr *= i
    return pr
