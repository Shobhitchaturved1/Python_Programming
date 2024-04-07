class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        ans=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visit:           
                    for dr,dc in directions:
                        row=r+dr
                        col=c+dc
                        if row<0 or row==ROWS or col<0 or col==COLS or grid[row][col]!=1:
                            ans+=1
                        visit.add((r,c))
        return ans                        