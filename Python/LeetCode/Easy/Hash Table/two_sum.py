from typing import List

class Solution:
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in nums:
            if nums[i] not in dict:
                dict
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], target = 9))
