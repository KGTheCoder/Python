from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
    
    def runningSum_2(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums):
            nums[i]+=nums[i-1]
            i+=1
        return nums 
    
    def runningSum_3(self, nums: List[int]) -> List[int]:
        res = [nums[0]] + [0] * (len(nums) - 1)
        for i, num in enumerate(nums[1:]):
            res[i + 1] += res[i] + num
        return res

    def runningSum_4(self, nums: List[int]) -> List[int]:
        res = []
        res.append(nums[0])
        for i in range(1, len(nums)):
            res.append(res[-1]+nums[i])
        return res


sol = Solution()
print(sol.runningSum_4([1,2,3,4]))