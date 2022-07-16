class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    
    def defangIPaddr_2(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

    def defangIPaddr_3(self, address: str) -> str:
        ans = []
        for ch in address:
            if ch.isdigit():
                ans.append(ch)
            else:
                ans.append("[.]")
        return "".join(ans)

sol = Solution()
# print(sol.defangIPaddr("1.1.1.1"))
# print(sol.defangIPaddr_2("1.1.1.1"))
# print(sol.defangIPaddr_3("1.1.1.1"))
