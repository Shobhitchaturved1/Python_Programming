class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit=set()
        nei=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    nei[i].append(j)
        count=0
        #print(nei)
        def dfs(node):
            visit.add(node)
            for i in nei[node]:
                if i not in visit:
                    dfs(i)
        for i in range(len(isConnected)):
            if i not in visit:
                count+=1
                dfs(i)
        return count        
