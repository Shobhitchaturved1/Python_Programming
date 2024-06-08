class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder={0:-1}
        Total=0
        for i,n in enumerate(nums):
            Total+=n
            r=Total%k
            if r not in remainder:
                remainder[r]=i
            elif i-remainder[r]>1:
                return True
        return False
                    