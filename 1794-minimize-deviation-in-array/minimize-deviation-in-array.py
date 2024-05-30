class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap,maxHeap=[],0
        for i in nums:
            tmp=i
            while i%2==0:
                i=i//2
            minHeap.append((i,max(tmp,2*i)))
            maxHeap=max(maxHeap,i)
        heapq.heapify(minHeap)   
        res=float("inf")
        while len(minHeap)==len(nums):
            n,nMax=heapq.heappop(minHeap)
            res=min(res,maxHeap-n)
            if n<nMax:
                heapq.heappush(minHeap,(n*2,nMax))
                maxHeap=max(maxHeap,n*2)
        return res        