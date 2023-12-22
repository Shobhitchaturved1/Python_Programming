class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=10**10
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            while(sum>=target):
                ans=min(ans,i-left+1)
                sum-=nums[left]
                left+=1
        if ans==10**10:
            return 0
        return ans            