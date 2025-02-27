class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp={}
        def solve(i,j):
            #Base Case
            if i<0:
                return j+1
            if j<0:
                return i+1
            if (i,j) in dp:
                return dp[(i,j)]        
            if word1[i]==word2[j]:
                dp[(i,j)]= 0+solve(i-1,j-1)
            else:
                dp[(i,j)]= min(1+solve(i,j-1), #for insert    
                    1+solve(i-1,j), #for delete
                    1+solve(i-1,j-1)) #for replace
            return dp[(i,j)]        
        return solve(m-1,n-1)    