class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        if len(nums)==1:return nums[0]
        nums[-2]=max(nums[-2],nums[-1])
        for i in range(len(nums)-3,-1,-1):
            nums[i]=max(nums[i+1],nums[i]+nums[i+2])
        return max(nums[0],nums[1])    