from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)

        for i in range(len(nums)):
            r = nums[i]

            b = nums[nums[i]] % q

            nums[i] = q * b + r

        for i in range(len(nums)):
            nums[i] = nums[i] // q 

        return nums

    def buildArray_2(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.append(nums[nums[i]])
        return res

    def buildArray_3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            nums[i] = nums[i]+(n*(nums[nums[i]]%n))

        for i in range(0, n):
            nums[i] = int(nums[i]/n)
        return nums

sol = Solution()
# print(sol.buildArray([0, 2, 1, 5, 3, 4]))
print(sol.buildArray_2([0, 2, 1, 5, 3, 4]))
print(sol.buildArray_3([0, 2, 1, 5, 3, 4]))