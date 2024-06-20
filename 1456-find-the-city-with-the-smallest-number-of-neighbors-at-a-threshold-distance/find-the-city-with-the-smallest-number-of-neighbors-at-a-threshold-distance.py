class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=defaultdict(list)
        for s,d,w in edges:
            adj[s].append((d,w))
            adj[d].append((s,w))
        count=float("inf")  
        res=0
        def dfs(node):
            ans=[float("inf")]*n
            ans[node]=0
            res=-1
            for i in range(n-1):
                for j in adj.keys():
                    tmpans=ans.copy()
                    for nei,w in adj[j]:
                        if ans[j]+w<=distanceThreshold:
                            tmpans[nei]=min(ans[nei],ans[j]+w)
                    ans=tmpans        
            for i in ans:
                if i!=float("inf"):
                    res+=1
            
            #print(ans)        
            return res                       
        for i in range(n):
            a=dfs(i)
            print(a)
            if count>=a:
                count=a
                res=i    
        return res       