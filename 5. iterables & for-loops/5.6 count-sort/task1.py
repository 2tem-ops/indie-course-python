nums = [int(i) for i in input()]
count = [0] * 10

for num in nums:
    count[num] += 1

for i in range(len(count)):
    if count[i] > 0:
        print(i, count[i])