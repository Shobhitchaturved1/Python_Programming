class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def rec(i,j):
            if i<0:
                return all(x == '*' for x in p[:j+1])
            if j<0:
                return i<0
            if (i,j) in dp:
                return dp[(i,j)]   
            if s[i]==p[j] or p[j]=="?":
                dp[(i,j)]= rec(i-1,j-1)
            elif p[j]=="*":
                dp[(i,j)]= rec(i- 1,j) or rec(i,j- 1)                      
            else:
                dp[(i,j)]= False
            return dp[(i,j)]    
        return rec(len(s)-1,len(p)-1)                    