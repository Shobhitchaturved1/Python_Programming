class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                res+=nums[i]
            else:
                ans=max(ans,res)
                res=nums[i]
        return max(ans,res)            