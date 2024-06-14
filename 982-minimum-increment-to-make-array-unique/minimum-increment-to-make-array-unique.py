class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increment=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                increment=nums[i-1]+1-nums[i]
                min_increment+=increment
                nums[i]=nums[i-1]+1
        return min_increment        