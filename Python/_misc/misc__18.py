"""
nums = [1, 2, 3, 4]
i = 1
while i < len(nums):
    nums[i]+=nums[i-1]
    i+=1

print(nums)
"""

nums = [1, 2, 3, 4]
res = [nums[0]] + [0] * (len(nums) - 1)
for i, num in enumerate(nums[1:]):
    res[i + 1] += res[i] + num

print(res)