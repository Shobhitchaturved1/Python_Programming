class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0,1,1]
        if n<=2:
            return dp[n]
        for i in range(3,n+1):
            ans=sum(dp)
            dp[0],dp[1]=dp[1],dp[2]
            dp[2]=ans
        return dp[-1]    