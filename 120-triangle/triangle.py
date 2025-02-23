class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            newdp=triangle[i]
            for i in range(len(newdp)):
                newdp[i]+=min(dp[i],dp[i+1])
            dp=newdp
        return dp[0]        