class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float("-inf")
        res=0
        for i in nums:
            res+=i
            if res<0:
                res=0
            ans=max(ans,res)
        if ans==0:
            return max(nums)   
        return ans        