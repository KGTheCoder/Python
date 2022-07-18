class Solution: 
    def removeVowels(self, s: str) -> str:
        ans = ""
        for letter in s:
            if letter not in "aeiou":
                ans += letter
        return ans

    def removeVowels_2(self, s: str) -> str:
        ans = []
        for letter in s:
            if letter not in "aeiou":
                ans.append(letter)
        return "".join(ans)

    def removeVowels_3(self, s: str) -> str:
        ans = []
        vowels = set("aeiou")
        for letter in s:
            if letter not in vowels:
                ans.append(letter)
        return "".join(ans)

sol = Solution()
# print(sol.removeVowels("This is a great message!"))
# print(sol.removeVowels_2("This is a great message!"))
print(sol.removeVowels_3("This is a great message!"))