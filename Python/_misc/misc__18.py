"""
nums = [1, 2, 3, 4]
i = 1
while i < len(nums):
    nums[i]+=nums[i-1]
    i+=1

print(nums)
"""

"""
nums = [1, 2, 3, 4]

print(nums[1:])

res = [nums[0]] + [0] * (len(nums) - 1)

print(res)

for i, num in enumerate(nums[1:]):
    res[i + 1] += res[i] + num

print(res)
"""

nums = [1, 2, 3, 4]

res = []
res.append(nums[0])

print(res)

for i in range(1, len(nums)):
    res.append(res[-1]+nums[i])
    print("i: " + str(i))
    print(res)

