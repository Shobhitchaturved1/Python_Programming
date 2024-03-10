class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        parent=[i for i in range(m*n)]
        rank=[1 for i in range(m*n)]
        def find(n):
            if parent[n]!=n:
                parent[n]=find(parent[n])
            return parent[n]  
        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1==p2:
                return 
            else:
                if rank[p1]<rank[p2]:
                    parent[p1]=p2
                    rank[p2]+=rank[p1]
                else:
                    parent[p2]=p1
                    rank[p1]+=rank[p2]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    x1=i*n+j
                    if(i+1<=m-1 and grid[i+1][j]=='1'):
                        x2=x1+n
                        union(x1,x2)
                    if(j+1<=n-1 and grid[i][j+1]=='1'):    
                        x2=x1+1
                        union(x1,x2)
                else:
                    rank[i*n+j]=0        
        ans=0
        for i in range(m*n):
            if find(i)==i and rank[i]>0:
                ans+=1
        return ans               