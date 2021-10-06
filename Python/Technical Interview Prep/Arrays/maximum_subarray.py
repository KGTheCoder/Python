from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        print(max_subarray)
        return max_subarray

sol = Solution()
sol.maxSubArray([5, 4, -1, 7, 8])
print(sol.maxSubArray)