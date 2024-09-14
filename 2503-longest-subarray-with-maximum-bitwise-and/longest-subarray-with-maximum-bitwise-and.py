class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        count=0
        cur=0
        for i in range(len(nums)):
            if nums[i]==maxi:
                cur+=1
            else:
                count=max(count,cur)
                cur=0
        return max(count,cur)            