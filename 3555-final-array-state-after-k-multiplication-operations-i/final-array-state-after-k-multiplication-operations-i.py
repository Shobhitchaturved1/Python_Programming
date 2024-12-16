class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            idx=0
            cur=0
            mini=float(inf)
            for num in nums:
                if num<mini:
                    mini=num
                    idx=cur
                cur+=1
            nums[idx]*=multiplier
        return nums            