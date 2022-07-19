from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(("+" in s) - ('-' in s) for s in operations)

sol = Solution()
print(sol.finalValueAfterOperations(["--X", "X++", "X++"]))