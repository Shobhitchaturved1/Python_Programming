class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        #Bob Simulation DFS
        bob_time={}  #At what time bob reaches the node
        def dfs(node,prev,time):
            if node==0:
                bob_time[node]=time 
                return True
            for nei in adj[node]:
                if nei==prev:
                    continue
                if dfs(nei,node,time+1):
                    bob_time[node]=time
                    return True
            return False
        dfs(bob,-1,0)
        #print(bob_time)

        #Alice Simulation BFS

        q=deque([(0,0,-1,amount[0])]) #node,time,parent,total_profit  
        res=float('-inf')         
        while q:
            node,time,parent,profit=q.popleft()
            for nei in adj[node]:
                if nei==parent:
                    continue
                nei_profit=amount[nei]
                nei_time=time+1
                if nei in bob_time:
                    if nei_time>bob_time[nei]:
                        nei_profit=0
                    if nei_time==bob_time[nei]:
                        nei_profit=nei_profit//2
                q.append((nei,nei_time,node,profit+nei_profit))
                if len(adj[nei])==1:
                    res=max(res,profit+nei_profit)    

        return res


        