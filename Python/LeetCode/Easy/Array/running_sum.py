from typing import List 

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        temp = []
        for i in range(0, len(nums)):
            temp = nums[i]
        
        return temp

    def runningSum_2(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

sol = Solution()
# print(sol.runningSum([1, 2, 3, 4]))
print(sol.runningSum_2([1, 2, 3, 4]))