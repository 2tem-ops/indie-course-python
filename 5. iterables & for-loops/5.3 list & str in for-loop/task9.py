# Делимость на 11

num = input()
even_ind = [int(i) for i in num[::2]]
odd_ind = [int(i) for i in num[1::2]]
print("YES" if abs(sum(even_ind) - sum(odd_ind)) % 11 == 0 else "NO")