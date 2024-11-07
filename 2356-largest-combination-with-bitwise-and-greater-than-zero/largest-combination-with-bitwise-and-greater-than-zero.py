class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        def countbits(nums,bit_position):
            if not nums:
                return 0
            if bit_position<0:
                return 0
            count=sum(1 for num in nums if (num&(1<<bit_position)))
            return max(count,countbits(nums,bit_position-1))
        return countbits(candidates,32)    