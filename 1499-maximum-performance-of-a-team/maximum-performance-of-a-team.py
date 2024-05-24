class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        egg=[]
        for eff,spd in zip(efficiency,speed):
            egg.append([eff,spd])
        egg.sort(reverse=True) 
        minHeap=[]
        res,speed=0,0
        for eff,spd in egg:
            if len(minHeap)==k:
                speed-=heapq.heappop(minHeap)
            speed+=spd
            heapq.heappush(minHeap,spd)
            res=max(res,eff*speed)   
        return res%(10**9+7)    