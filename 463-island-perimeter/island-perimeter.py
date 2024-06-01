class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        ans=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    for dr,dc in directions:
                        row,col=r+dr,c+dc
                        if row<0 or row==rows or col<0 or col==cols or grid[row][col]!=1:
                            ans+=1
                        visit.add((r,c))
        return ans                    
