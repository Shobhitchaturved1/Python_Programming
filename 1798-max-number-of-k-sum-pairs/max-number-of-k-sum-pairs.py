class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diff=Counter(nums)
        count=0
        nums=set(nums)
        for i in nums:
            if k-i in diff:
                count+=min(diff[i],diff[k-i])
        return count//2             