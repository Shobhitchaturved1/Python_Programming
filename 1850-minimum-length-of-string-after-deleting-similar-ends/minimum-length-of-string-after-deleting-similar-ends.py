class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        if len(s)<=1:
            return len(s)
        while i<j:
            if s[i]!=s[j]:
                return j-i+1
            else:
                while(s[i]==s[j] and i!=j):
                    i+=1
                while(s[i-1]==s[j] and i!=j):
                    j-=1
                if i==j and s[i-1]!=s[j]:
                    return 1    
        return 0                    