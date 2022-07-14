from typing import List

class Solution:
    def sumZero(self, n):
        return range(1 - n, n, 2)
    
    def sumZero_2(self, n):
        out = []
        while n:
            if n % 2 == 0:
                out.append(n/2)
                out.append(-n/2)
                n-=2
            else:
                out.append(0)
                n-=1
        return out
    
    def sumZero_3(self, n):
        ans, end = [], n
        if n % 2:
            ans.append(0)
            end-=1
        for i in range(1, end//2+1):
            ans.extend([i, -i])
        return ans



sol = Solution()
# print(sol.sumZero(2))
print(sol.sumZero_2(3))
# print(sol.sumZero_3(5))
