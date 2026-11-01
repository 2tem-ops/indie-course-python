def find_duplicate(nums: list[int]) -> list[int]:
    res = []
    for num in nums:
        if num not in res and nums.count(num) > 1:
            res.append(num)
    return res

print(find_duplicate([1, 2, 3, 4]))