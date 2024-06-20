class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for s,d,t in roads:
            adj[s].append((d,t))
            adj[d].append((s,t))
        start=0
        end=n-1    
        min_dist={i:[float("inf"),0] for i in adj.keys()}
        min_dist[start]=[0,1]    
        heap=[(0,start)] #time,source
        while heap:
            time,node=heapq.heappop(heap)
            if time>min_dist[end][0]:
                break
            for nei,t in adj[node]:
                if(time+t)>min_dist[nei][0]:
                    continue
                elif (time+t)==min_dist[nei][0]:
                    min_dist[nei][1]+=min_dist[node][1]
                else:
                    min_dist[nei][0]=time+t
                    min_dist[nei][1]=min_dist[node][1]
                    heappush(heap,(time+t,nei)) 
        return min_dist[end][1]%(10**9+7)                             
