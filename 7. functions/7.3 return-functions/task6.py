def first_unique_char(text: str) -> int:
    found = [i for i in text if text.count(i) == 1]
    if found: return text.find(found[0])
    return -1
