class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
            return len(visit)==n
        for i in range(n):
            visit=set()
            visit.add(i)
            if dfs(i):return i
        return -1    
