from typing import List

class Solution: 
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        num = 0

        for v in nums:
            if v in repeat:
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                repeat[v] += 1
            else:
                repeat[v] = 1
        return num

    def numIdenticalPairs_2(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res

sol = Solution()
print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(sol.numIdenticalPairs_2([1, 2, 3, 1, 1, 3]))
