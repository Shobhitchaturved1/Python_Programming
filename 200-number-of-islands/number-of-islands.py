class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        ans=0
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col=q.popleft()
                direction=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in direction:
                    r,c=row+dr,col+dc
                    if(0<=r<rows and 0<=c<cols and grid[r][c]=="1" 
                        and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]=="1":
                    bfs(r,c)
                    ans+=1
        return ans            