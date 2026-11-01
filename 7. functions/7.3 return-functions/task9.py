# Сколько нулей на конце факториала N!

from math import factorial

def trailing_zeros(num: int) -> int:
    work = str(factorial(num))[::-1]
    res = []
    for i in range(len(work)):
        remove = work[0]
        if remove == "0":
            res.append(remove)
            work = work[1:]
        else:
            break
    return len(res)

print(trailing_zeros(0))