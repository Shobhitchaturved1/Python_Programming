class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if (0>r or 0>c or r==ROW or c==COL or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            res=1
            direction=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in direction:
                row,col=r+dr,c+dc
                res+=dfs(row,col)
            return res        
        land,borderland=0,0
        for r in range(ROW):
            for c in range(COL):
                land+=grid[r][c]
                if (grid[r][c]==1 and 
                (r,c) not in visit and 
                (r in [0,ROW-1] or c in [0,COL-1] )):
                    borderland+=dfs(r,c)
        return land-borderland            