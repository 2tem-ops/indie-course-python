# A. Фотографии Брейна

n, m = map(int, input().split())
photo = [[*input().replace(" ", "")] for _ in range(n)]
flag = True
correct = "WGB"

for row in photo:
    for pixel in row:
        if pixel not in correct:
            flag = False
            break
    if not flag:
        break

print("#Black&White" if flag else "#Color")
