class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l=0
        for i in range(len(s)):
            if s[i]==t[l]:
                l+=1
            if l==len(t):
                return 0
        return len(t)-l            