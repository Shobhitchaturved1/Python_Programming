class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            p1,p2=find(x),find(y)
            if p1==p2:
                rank[p2]+=1
                return
            if rank[p1]<rank[p2]:
                parent[p1]=p2
                rank[p2]+=rank[p1]+1
            else:
                parent[p2]=p1
                rank[p1]+=rank[p2]+1
        parent=[i for i in range(m*n)] 
        rank=[0]*(m*n)
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    union(i,j+m)
        ans=0
        for i in range(m*n):
            if parent[i]==i and rank[i]>1:
                ans+=rank[i]
        return ans                    
