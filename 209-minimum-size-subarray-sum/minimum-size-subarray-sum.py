class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        res=0
        window=len(nums)
        i=0
        j=0
        while i<len(nums) and j<len(nums):
            res+=nums[j]
            if res>=target:
                while res>=target:
                    window=min(window,j-i+1)
                    res-=nums[i]
                    i+=1      
            j+=1        
        return window                
