class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        ans=1
        dp[-1]=1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
            if dp[i]==0:
                dp[i]=1        
            ans=max(ans,dp[i])
        return ans        
