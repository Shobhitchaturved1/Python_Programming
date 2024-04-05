class Solution:
    def check(self, nums: List[int]) -> bool:
        # Initialize the break variable to 0
        breaks = 0

        # Iterate over the len(nums)
        for i in range(len(nums)):
            # If you find any break case, increment the break variable
            if nums[i] < nums[i-1]:
                breaks += 1
        
        # If there is atmost 1 breaks, return True
        # Else, return False
        return True if breaks <= 1 else False