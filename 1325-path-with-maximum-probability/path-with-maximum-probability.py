class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=defaultdict(list)
        for i,z in zip(edges,succProb):
            adj[i[0]].append([z,i[1]])
            adj[i[1]].append([z,i[0]])
        minheap=[[0,start_node]]
        visit=set()
        while minheap:    
            prob,node=heapq.heappop(minheap)
            visit.add((node))
            if node==end_node:
                return -prob
            for p,nei in adj[node]:
                if prob==0 and nei not in visit:
                    heapq.heappush(minheap,[-p,nei]) 
                elif prob!=0 and nei not in visit:
                    heapq.heappush(minheap,[prob*p,nei])
        return 0                 