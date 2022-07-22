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
    
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
    
    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            try:
                return [hashMap[target - n], i]
            except:
                hashMap[n] = i
    
    def twoSum_4(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            else:
                dic[target - n] = i



sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], target = 9))
print(sol.twoSum_4([2, 7, 11, 15], target = 9))