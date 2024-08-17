class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        res=[]
        for src,des in tickets:
            adj[src].append(des)
        for key in adj:
            adj[key].sort()
        def dfs(adj,result,src):
            if src in adj:
                destinations=adj[src][:]
                while destinations:
                    dest=destinations[0]
                    adj[src].pop(0)
                    dfs(adj,res,dest)
                    destinations=adj[src][:]
            res.append(src)
        dfs(adj,res,"JFK")
        res.reverse()
        if len(res)!=len(tickets)+1:
            return []
        return res                       