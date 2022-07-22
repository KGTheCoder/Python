class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        map = {}
        temp = "a"
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
    
    def decodeMessage_2(self, key: str, message: str) -> str:
        hashT = {" ": " "}
        i = 97
        for k in key:
            if k not in hashT and k != ' ':
                hashT[k] = chr(i)
                i += 1
        return "".join(hashT[m] for m in message)
    
    def decodeMessage_3(self, key: str, message: str) -> str:
        dic = {}
        seq = 97
        res = ""

        for c in key:
            if c not in dic and c != " ":
                dic[c] = dic.get(c, 0)
        for v in dic:
            dic[v] = chr(seq)
            if seq <= 122:
                seq += 1
            else:
                seq = 97
        for c in message:
            if c == " ":
                res += " "
            else:
                res += dic[c]

        return res
    
    def decodeMessage_4(self, key: str, message: str) -> str:
        d = {}
        String = ''
        res = ''

        for k in key: 
            if k != ' ' and k not in String:
                String += k
        for i, ch in enumerate(String):
            if ch not in d:
                d[ch] = chr(97 + i)
        for m in message:
            if m.isalpha():
                res += d[m]
            elif m == ' ':
                res += ' '

        return res


sol = Solution()
# print(sol.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
print(sol.decodeMessage_4("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))