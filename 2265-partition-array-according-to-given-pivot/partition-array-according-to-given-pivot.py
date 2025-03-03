class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        idx = 0
        
        # Place elements less than pivot
        for num in nums:
            if num < pivot:
                result[idx] = num
                idx += 1
        
        # Place elements equal to pivot
        for num in nums:
            if num == pivot:
                result[idx] = num
                idx += 1
        
        # Place elements greater than pivot
        for num in nums:
            if num > pivot:
                result[idx] = num
                idx += 1
        
        # Copy result back to nums in-place
        nums[:] = result
        return nums