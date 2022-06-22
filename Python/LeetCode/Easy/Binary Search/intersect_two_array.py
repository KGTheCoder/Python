class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        return res

solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1, nums2)) 
