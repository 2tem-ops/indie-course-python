password, repeat = input(), input()

if len(password) < 7:
    print("Short")
elif password != repeat:
    print("Difference")
else:
    print("OK")