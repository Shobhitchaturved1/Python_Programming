class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans=0
        l=0
        for i in range(len(nums)):
            if nums[l]<=nums[i]:
                l=i
                ans+=1
        return ans        