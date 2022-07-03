from typing import List 

class Solution: 
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = []
        for i in range(0, 2*n):
            if i < n:
                r.append(nums[i])
            else:
                r.append(nums[i-n])
        return r

    


ans = Solution()
print(ans.getConcatenation([1, 2, 1]))
print(ans.getConcatenation2([1, 2, 1]))
