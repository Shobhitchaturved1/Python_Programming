class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        zero=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1        
            res=r-l if zero else r-l+1    
            ans=max(ans,res)
        return ans if ans!=len(nums) else ans-1      