def count_AGTC(dna: str) -> tuple[int, ...]:
    count = {"A": 0, "G": 0, "T": 0, "C": 0}
    for char in dna: count[char] += 1
    return tuple(count.values())
