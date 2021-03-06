from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            expect = target - nums[i]
            if expect in nums and i != nums.index(expect):
                return [i, nums.index(expect)]


nums = [2, 7, 11, 15]
sol = Solution()
print(sol.twoSum(nums, 9))