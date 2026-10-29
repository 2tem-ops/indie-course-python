for i in range((a := int(input())), (b := int(input())) + 1):
    res = ""
    if i % 3 == 0: res += "Fizz"
    if i % 5 == 0: res += "Buzz"
    print(res if res else i)