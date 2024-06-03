class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols=len(grid1),len(grid1[0])
        visit=set()
        count=0
        def dfs(r,c):
            if(r not in range(rows) or
               c not in range(cols) or
               (r,c) in visit or
               grid2[r][c]==0):
               return 0
            elif (grid1[r][c]==0 and grid2[r][c]==1):
                return 1
            visit.add((r,c))    
            return 0 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c]==1 and (r,c) not in visit:
                    if not dfs(r,c):
                        count+=1
        return count                
