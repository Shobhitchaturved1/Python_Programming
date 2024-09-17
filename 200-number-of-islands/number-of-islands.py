class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        ROW,COL=len(grid),len(grid[0])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        count=0
        def dfs(r,c):
            visit.add((r,c))
            for dr,dc in direction:
                row,col=dr+r,dc+c
                if(0<=row<ROW and 0<=col<COL and grid[row][col]=="1"
                   and (row,col) not in visit):
                   dfs(row,col)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]=="1" and (r,c) not in visit:
                    count+=1
                    dfs(r,c)
        return count             