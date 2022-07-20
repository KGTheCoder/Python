from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(("+" in s) - ('-' in s) for s in operations)

    def finalValueAfterOperations_2(self, operations: List[str]) -> int:
        return sum(1 if "+" in i else -1 for i in operations)
    
    def finalValueAfterOperations_3(self, operations: List[str]) -> int:
        return sum(-1 if i in "--X--" else 1 for i in operations)

    def finalValueAfterOperations_4(self, operations: List[str]) -> int:
        return len(operations) - str(operations).count("-")
    
    def finalValueAfterOperations_5(self, operations: List[str]) -> int:
        return sum(-1 if i[1] == "-" else 1 for i in operations)

    def finalValueAfterOperations_6(self, operations: List[str]) -> int:
        op_dict = {"--X" : -1, "X--" : -1, "X++" : 1, "++X" : 1}
        return sum(op_dict[op] for op in operations)
    
    def finalValueAfterOperations_7(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if o[1] == "+":
                x += 1
            else:
                x -= 1
        return x

    def finalValueAfterOperations_8(self, operations: List[str]) -> int:
        mydict = {"++X":1, "X++":1, "--X":-1, "X--":-1}
        val = 0
        for op in operations:
            val += mydict[op]
        return val

    def finalValueAfterOperations_9(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == "++X" or i =="X++":
                x += 1
            else:
                x -= 1
        return x

sol = Solution()
print(sol.finalValueAfterOperations_9(["X++", "++X", "--X", "X--"]))