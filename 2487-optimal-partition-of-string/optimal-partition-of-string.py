class Solution:
    def partitionString(self, s: str) -> int:
        count=0
        sub=s[0]
        for r in range(len(s)):
            if s[r] in sub:
                count+=1
                sub=s[r]
            else:
                sub+=s[r]
        return count             