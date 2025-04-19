class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() # order does not matter as [i]+[j] = [j]+[i]
        count = 0
        for i in range(len(nums)): # for each [i] find [j] in [i + 1, N)
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1) - 1
            count += right - left + 1
        return count