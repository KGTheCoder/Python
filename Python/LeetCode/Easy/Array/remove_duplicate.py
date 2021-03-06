from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        if len(nums) == 0: return length 
        for i in range(1, len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length + 1

sol = Solution()
print(sol.removeDuplicates([1, 2, 2]))
 