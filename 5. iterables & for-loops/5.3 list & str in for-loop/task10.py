# Правильная скобочная последовательность

brackets, count = input(), 0

for i in range(len(brackets)):
    if count == -1:
        break
    if brackets[i] == '(': count += 1
    if brackets[i] == ')': count -= 1

print("YES" if count == 0 else "NO")