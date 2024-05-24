class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[-int(n) for n in nums]
        heapq.heapify(nums)
        while k:
            a=heapq.heappop(nums)
            k-=1
        return str(-a)    