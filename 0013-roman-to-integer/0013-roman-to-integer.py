class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t = 0
        for i in range(len(s)):
            if i<len(s)-1 and d[s[i]] < d[s[i+1]]:
                t -= d[s[i]]
            else:
                t += d[s[i]]
        return t