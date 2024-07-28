class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj=defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        q=deque([1])
        visit_time=defaultdict(list)
        cur_time=0
        res=-1
        while q:
            for i in range(len(q)):    
                node=q.popleft()
                if node==n:
                    if res!=-1:
                        return cur_time
                    res=cur_time
                for nei in adj[node]:
                    nei_time=visit_time[nei]
                    if len(nei_time)==0 or (len(nei_time)==1 and nei_time[0]!=cur_time):
                        q.append(nei)
                        nei_time.append(cur_time)
            
            if (cur_time//change)%2==1:
                cur_time+=change-(cur_time%change)
            cur_time+=time