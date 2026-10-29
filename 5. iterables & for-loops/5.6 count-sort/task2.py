input()
nums = list(map(int, input().split()))
count = [0] * 201

for num in nums:
    count[num + 100] += 1

for i in range(len(count)):
    if count[i] > 0:
        print((str(i - 100) + " ") * count[i], end="")