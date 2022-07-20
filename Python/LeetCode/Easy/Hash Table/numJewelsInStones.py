class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
    
    def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)

    def numJewelsInStones_3(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))
    
    def numJewelsInStones_4(self, j: str, s: str) -> int:
        return sum(map(s.count, j))
    
    def numJewelsInStones_5(self, J, S):
        charToFreqS = {}
        numJewels = 0

        for ch in S:
            if ch not in charToFreqS:
                charToFreqS[ch] = 1
            else:
                charToFreqS[ch] += 1
        
        for ch in J:
            if ch in charToFreqS:
                numJewels += charToFreqS[ch]
        
        return numJewels

sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))
print(sol.numJewelsInStones_5("aA", "aAAbbbb"))