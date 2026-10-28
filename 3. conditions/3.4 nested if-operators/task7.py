# Кнопочные гонки

s, v1, v2, t1, t2 = map(int, input().split())

w1 = s * v1 + 2 * t1
w2 = s * v2 + 2 * t2

if w1 > w2:
    print("Second")
elif w2 > w1:
    print("First")
else:
    print("Friendship")