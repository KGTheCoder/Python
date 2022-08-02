class Solution: 
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        for i, n in enumerate(a):
            n = n[::-1]
            a[i] = n
        s = ' '.join(a)
        return s
    
    def reverseWords_2(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])

    def reverseWords_3(self, s: str) -> str:
        words = list(s.split(" "))
        result = ''
        for index in range(len(words)):
            result += words[index][::-1]
            if index != len(words)-1:
                result += " "
        return result 


sol = Solution()
print(sol.reverseWords_3('Let\'s take LeetCode contest'))
