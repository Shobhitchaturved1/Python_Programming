class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax=0
        globalMax=nums[0]
        curMin=0
        globalMin=nums[0]
        Total=0
        for i in nums:
            Total+=i
            curMax=max(curMax+i,i)
            curMin=min(curMin+i,i)
            globalMin=min(globalMin,curMin)
            globalMax=max(globalMax,curMax)
        return max(Total-globalMin,globalMax)if globalMax>0 else globalMax    