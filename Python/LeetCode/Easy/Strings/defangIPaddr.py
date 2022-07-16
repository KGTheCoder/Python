class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    
    def defangIPaddr_2(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

sol = Solution()
# print(sol.defangIPaddr("1.1.1.1"))
print(sol.defangIPaddr_2("1.1.1.1"))