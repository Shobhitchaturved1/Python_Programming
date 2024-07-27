class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj=defaultdict(list)
        for i in range(len(original)):
            adj[original[i]].append((cost[i],changed[i]))
        cost=0  
        dp=defaultdict(int)
        #print(adj)  
        def dfs(s,t):
            minheap=[(0,s)]
            visit=set()
            while minheap:
                c,w=heapq.heappop(minheap)
                visit.add(w)
                if w==t:
                    return c
                for cost,i in adj[w]:
                    if i not in visit:
                        heapq.heappush(minheap,(cost+c,i))  
            return -1             
        for i in range(len(source)):
            if (source[i],target[i]) in dp:
                cost+=dp[(source[i],target[i])]
            if source[i]!=target[i] and (source[i],target[i]) not in dp:
                c=dfs(source[i],target[i]) 
                dp[(source[i],target[i])]=c
                #print(c)  
                if c==-1:
                    return -1
                else:
                    cost+=c    
        return cost         