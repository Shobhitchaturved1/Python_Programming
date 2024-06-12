class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        dis=-1
        q=deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    q.append([r,c])
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            r,c=q.popleft()  
            dis=grid[r][c]          
            for dr,dc in direction:
                row,col=r+dr,c+dc
                if (0<=row<ROW and 0<=col<COL and grid[row][col]==0):
                    q.append([row,col])
                    grid[row][col]=1+grid[r][c]
        return dis-1 if dis>1 else -1            