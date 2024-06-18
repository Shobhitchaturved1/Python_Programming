class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans=0
        maxheap=[]
        for diff,pro in zip(difficulty,profit):
            maxheap.append((diff,pro))
        heapq.heapify(maxheap) 
        maxpro=[]
        worker.sort()
        i=0
        while i<len(worker):
            while maxheap and maxheap[0][0]<=worker[i]:
                diff,pro=heapq.heappop(maxheap)
                if diff<=worker[i]:
                    heapq.heappush(maxpro,-pro)  
            if maxpro:
                #print(maxpro)
                ans+=-1*maxpro[0]
            i+=1        
        return ans    