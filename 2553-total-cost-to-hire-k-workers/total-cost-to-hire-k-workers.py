class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) <= 2*candidates:  
            return sum(sorted(costs)[:k])
        heap1=costs[:candidates]
        heap2=costs[-candidates:]
        ans=0
        l=candidates
        r=len(costs)-candidates-1
        heapify(heap1)
        heapify(heap2)
        while k:
            if heap1 and (not heap2 or heap1[0] <= heap2[0]):
                ans += heappop(heap1)
                if l <= r:  # Add new candidate from the middle
                    heappush(heap1, costs[l])
                    l += 1
            else:
                ans += heappop(heap2)
                if r >= l:  # Add new candidate from the middle
                    heappush(heap2, costs[r])
                    r -= 1
            k -= 1
        return ans                

