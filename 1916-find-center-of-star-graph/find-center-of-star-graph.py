class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        for i in adj.keys():
            if len(adj[i])==len(edges):
                return i    