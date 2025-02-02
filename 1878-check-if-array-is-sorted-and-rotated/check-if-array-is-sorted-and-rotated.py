class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks = 0

        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                breaks += 1
        
        return True if breaks <= 1 else False