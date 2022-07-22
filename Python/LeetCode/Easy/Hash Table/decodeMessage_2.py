class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        d = {}
        String = ''
        
        res = ''
        for k in key:
            if k !=' ' and k not in String:
                String += k
        for i, ch in enumerate(String):
            if ch not in d:
                d[ch] = chr(97 + i)   
        for m in message:
            if m.isalpha(): ## This if is needed to ignore the spaces.
                res += d[m]
            elif m ==' ': ## Keep the Spaces in its original place.
                res += ' '
        return res

sol = Solution()
print(sol.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))