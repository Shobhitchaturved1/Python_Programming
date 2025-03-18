class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l,r=0,0
        ans=0
        for l in range(len(nums)):
            r=l
            a=nums[l]
            while r+1<len(nums) and (a & nums[r+1])==0:
                a=a | nums[r+1] 
                r+=1
            ans=max(ans,r-l+1)
        return ans        