class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)

        #Tabulation
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j  
        for i in range(1,m+1):
            for j in range(1,n+1):  
                if word1[i-1]==word2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j]= min(1+dp[i][j-1], #for insert    
                                1+dp[i-1][j], #for delete
                                1+dp[i-1][j-1]) #for replace
        return dp[m][n]
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