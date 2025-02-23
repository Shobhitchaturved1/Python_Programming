class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp=matrix[-1]
        for i in range(len(matrix)-2,-1,-1):
            newdp=matrix[i]
            for j in range(len(matrix[0])):
                c=dp[j]
                if j-1>=0:
                    c=min(c,dp[j-1])
                if j+1<len(matrix[0]):
                    c=min(c,dp[j+1])
                newdp[j]+=c
            dp=newdp
        return min(dp)            
