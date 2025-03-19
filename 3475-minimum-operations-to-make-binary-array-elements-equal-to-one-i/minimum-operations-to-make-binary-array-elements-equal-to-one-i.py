class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=1
                count+=1
                if i+2<len(nums):
                    nums[i+1]=0 if nums[i+1] else 1
                    nums[i+2]=0 if nums[i+2] else 1
                else:
                    return -1
        return count                