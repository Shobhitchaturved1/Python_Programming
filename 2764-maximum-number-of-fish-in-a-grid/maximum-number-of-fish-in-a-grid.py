class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        ans=0
        
        
        def dfs(r,c):
            if(min(r,c)<0 or r==ROW or c==COL or (r,c) in visit or grid[r][c]==0):
                return 0
            visit.add((r,c))
            return grid[r][c]+(dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))    

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]>0:
                    visit=set()
                    ans=max(ans,dfs(r,c))
        return ans            