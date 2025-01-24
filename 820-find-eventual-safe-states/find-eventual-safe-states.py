class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        visit=set()
        for i in range(len(graph)):
            if len(graph[i])==0:
                visit.add(i)
                continue
            for j in graph[i]:
                adj[i].append(j)
        ans=[]  
        path=set()      
        def check(node):
            if node in visit:
                return True
            if node in path:
                return False    
            path.add(node)
            for nei in adj[node]:
                if not check(nei):
                    return False
            path.remove(node)
            visit.add(node)
            return True        
        for i in range(len(graph)):
            if check(i):
                ans.append(i)
        return ans        