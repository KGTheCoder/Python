class Solution: 
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
    
    def romanToInt_2(self, s: str) -> int:
        res, prev = 0, 0
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:
            if values[i] >= prev:
                res += values[i]
            else:
                res -= values[i]
            prev = values[i]
        return res

sol = Solution()
# print(sol.romanToInt("III"))
print(sol.romanToInt_2("III"))