class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N=len(grid)
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def out_of_bound(r,c):
            return (min(r,c)<0 or r==N or c==N)
        size=defaultdict(int)
        def dfs(r,c,label):
            if(out_of_bound(r,c) or grid[r][c]!=1):
                return 0
            size=1
            grid[r][c]=label
            for nr,nc in directions:
                size+=dfs(nr+r,nc+c,label)
            return size
        label=2    
        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    size[label]=dfs(r,c,label)
                    label+=1

        def connect(r,c):
            visit=set()
            res=1
            for nr,nc in directions:
                if not out_of_bound(nr+r,nc+c) and grid[nr+r][nc+c] not in visit:
                    visit.add(grid[nr+r][nc+c]) 
                    res+=size[grid[nr+r][nc+c]]
            return res                  
        res=0 if not size else max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c]==0:
                    res=max(res,connect(r,c))
        return res            