class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
    
    def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)

    def numJewelsInStones_3(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))

sol = Solution()
# print(sol.numJewelsInStones("aAabbA", "BbaAabAAb"))
# print(sol.numJewelsInStones_2("aAabbA", "BbaAabAAb"))
print(sol.numJewelsInStones_3("aAabbA", "BbaAabAAb"))