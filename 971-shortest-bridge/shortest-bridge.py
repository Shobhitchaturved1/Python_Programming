class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if(r<0 or r==ROW or c<0 or c==COL or grid[r][c]!=1 or (r,c) in visit):
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        def bfs():
            res,q=0,deque(visit)
            direction=[[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in direction:
                        row,col=r+dr,c+dc
                        if(row<0 or row==ROW or col<0 or col==COL or (row,col) in visit):
                            continue
                        if grid[row][col]:
                            return res
                        q.append([row,col])        
                        visit.add((row,col))
                res+=1        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    dfs(r,c)
                    return bfs()