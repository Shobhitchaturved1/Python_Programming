class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        ans=0
        visit=set()
        def dfs(r,c):
            if(r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]!=0):
                return
            grid[r][c]=2
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0 and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    dfs(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0 and (r,c) not in visit:
                    dfs(r,c)
                    ans+=1
        return ans                        