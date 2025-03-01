class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count_zero=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0 
            if nums[i]==0:
                count_zero+=1 
        if nums[-1]==0:count_zero+=1                  
        nums=[i for i in nums if i!=0]
        return nums+[0]*count_zero           
                            