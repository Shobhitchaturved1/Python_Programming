class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp={}
        def solve(i):
            if i==n:
                return 0
            if i in dp:
                return dp[i]    
            leng=0
            maxi=float("-inf")   
            ans=float("-inf")  
            for j in range(i,min(n,i+k)):
                leng+=1
                maxi=max(maxi,arr[j])
                cost=maxi*leng + solve(j+1)
                ans=max(ans,cost)
            dp[i]=ans    
            return ans    
        return solve(0)    
