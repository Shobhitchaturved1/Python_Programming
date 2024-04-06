class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit=set()
        rows,cols=len(grid),len(grid[0])
        ans=0
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if(0<=r<rows and 0<=c<cols and
                        grid[r][c]=="1" and
                        (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    ans+=1    
        return ans            