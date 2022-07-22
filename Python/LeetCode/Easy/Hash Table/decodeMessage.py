class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        map = {}
        temp = 'a'
        for i in range(len(key)):
            if key[i] != " " and map.get(key[i]) == None:
                map[key[i]] = temp
                temp = chr(ord(temp) + 1)
        ans = ""
        for i in range(len(message)):
            if message[i] != " ":
                ans += map[message[i]]
            else:
                ans += " "
        return ans

sol = Solution()
print(sol.decodeMessage('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv'))