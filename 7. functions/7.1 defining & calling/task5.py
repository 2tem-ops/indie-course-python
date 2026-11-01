def sum_num(n: str) -> None:
    print(sum(int(i) for i in n if i.isdigit()))