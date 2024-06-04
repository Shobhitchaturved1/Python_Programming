class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        preMap=defaultdict(list)
        ans=[]
        visit=set()
        for i in range(len(graph)):
            for j in graph[i]:
                preMap[i].append(j)
        #print(preMap)        
        def dfs(i):
            if i in visit:
                return False
            if preMap[i]==[]:
                return True
            visit.add(i)    
            for pre in preMap[i]:
                if not dfs(pre):return False
            visit.remove(i)    
            preMap[i]=[]    
            return True                    
        for i in range(len(graph)):
            if dfs(i):ans.append(i)
        return ans            