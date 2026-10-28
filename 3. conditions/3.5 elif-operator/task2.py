res = ""

if (num := int(input())) % 3 == 0:
    res += "Fizz"
if num % 5 == 0:
    res += "Buzz"

print(res if res else num)