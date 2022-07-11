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

    def runningSum_3(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result

    def runningSum_4(self, nums: List[int]) -> List[int]:
        result = []
        result.append(nums[0])
        for i in range(1, len(nums)):
            result.append(result[-1]+nums[i])
        return result

sol = Solution()
# print(sol.runningSum([1, 2, 3, 4]))
# print(sol.runningSum_2([1, 2, 3, 4]))
# print(sol.runningSum_3([1, 2, 3, 4]))
print(sol.runningSum_4([1, 2, 3, 4]))