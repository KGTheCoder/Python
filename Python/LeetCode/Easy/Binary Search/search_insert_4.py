import bisect 

class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)

arr = [1, 3, 5, 6]
solution = Solution()
print(solution.searchInsert(arr, 5))