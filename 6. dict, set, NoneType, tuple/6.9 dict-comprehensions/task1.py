nums = [int(i) for i in input().split(",")]
print({nums.index(num): num for num in nums if nums.index(num) % 2 == 0})