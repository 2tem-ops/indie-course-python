data = [1, 2, "hello", 0, 3, 4, None, 5]

print(sum(i for i in data if type(i) in (int, float)))