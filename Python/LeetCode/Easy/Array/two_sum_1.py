from typing import List 

class Solution:
    def twoSum(self, nums, target) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

solution = Solution()
nums, target = [3, 2, 4], 6
print(solution.twoSum(nums, target))