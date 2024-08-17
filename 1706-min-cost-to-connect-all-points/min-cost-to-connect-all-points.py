class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        adj={i:[] for i in range(N)}
        for i in range(N):
            x,y=points[i]
            for j in range(i+1,N):
                x2,y2=points[j]
                dist=abs(x-x2)+abs(y-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        res=0
        minheap=[[0,0]]
        visit=set()
        while len(visit)<N:
            c,i=heapq.heappop(minheap)
            if i in visit:
                continue
            res+=c
            visit.add(i)
            for dis,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,[dis,nei])
        return res            