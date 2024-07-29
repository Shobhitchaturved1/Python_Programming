class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        res=[]
        heap=[]
        for i in set(nums):
            heapq.heappush(heap,[-1*hashmap[i],i])
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res         