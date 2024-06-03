class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        if not grid:return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if (r not in range(rows) or(c not in range(cols)) or grid[r][c]=="0" or (r,c) in visit):
                return
            visit.add((r,c))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    count+=1
                    dfs(r,c)            
        return count                   