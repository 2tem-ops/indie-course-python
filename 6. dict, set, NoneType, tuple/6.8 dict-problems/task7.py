nums = list(map(int, input().split()))

def nested_dict(lst: list[int]) -> dict:
    if len(lst) == 2:
        return {lst[0]: lst[1]}

    if len(lst) < 2:
        return {}

    return {lst[0]: nested_dict(lst[1:])}

print(nested_dict(nums))