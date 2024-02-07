class Solution:
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        0 : 0
    }
    def __init__(self, s):
        self.s = s
    
    def romanToInt(self):
        result = list()
        s = list(self.s.upper())
        for num in range(len(s)):
            if s[num] == "I" and num != len(s)-1:
                if s[num+1] in ("V", "X"):
                    answer = self.roman[s[num+1]] - self.roman[s[num]]
                    result.append(answer)
                    s[num+1] = 0
                else:
                    answer = self.roman[s[num]]
                    result.append(answer)
            elif s[num] == "X" and num != len(s)-1:
                if s[num+1] in ("L", "C"):
                    answer = self.roman[s[num+1]] - self.roman[s[num]]
                    result.append(answer)
                    s[num+1] = 0
                else:
                    answer = self.roman[s[num]]
                    result.append(answer)
            elif s[num] == "C" and num != len(s)-1:
                if s[num+1] in ("D", "M"):
                    answer = self.roman[s[num+1]] - self.roman[s[num]]
                    result.append(answer)
                    s[num+1] = 0
                else:
                    answer = self.roman[s[num]]
                    result.append(answer)
            else:
                answer = self.roman[s[num]]
                result.append(answer)
        return print(sum(result))

    def romanToIntNW(self):
            s = list(self.s.upper())

frst = Solution("iii")
frst.romanToInt()

scnd = Solution("lviii")
scnd.romanToInt()

thrd = Solution("MCMXCIV")
thrd.romanToInt()