s = input()
data = {digit: s.count(digit) for digit in s if digit.isdigit() and s.count(digit) > 1}
print(*sorted(data) if data else ["NO"])