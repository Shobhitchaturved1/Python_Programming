class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr=[0]+nums.copy()
        for i in range(len(nums)-1):
            n=nums[i]
            for j in range(i+1,len(nums)):
                n+=nums[j]
                subarr.append(n)
        subarr.sort()
        return sum(subarr[left:right+1])%(10**9+7)  