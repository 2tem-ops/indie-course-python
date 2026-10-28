nums = list(map(int, input().split()))

while nums.count(5) < 10: nums.append(5)
print([num for num in nums if num != 4 and num != 7])