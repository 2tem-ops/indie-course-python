def format_name_list(name_list: list[dict]) -> str:
    res = [value for dictionary in name_list for value in dictionary.values()]
    if len(res) > 1:
        return ", ".join(res[:-1]) + " и " + res[-1]
    return res[0]