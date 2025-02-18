class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans=0
        for i in range(k):
            if s[i] in "aeiou":
                ans+=1   
        l=0
        r=k
        count=ans
        while r<len(s):
            if s[l] in "aeiou":
                count-=1
            l+=1
            if s[r] in "aeiou":
                count+=1
                ans=max(ans,count)
            r+=1
        return max(ans,count)            