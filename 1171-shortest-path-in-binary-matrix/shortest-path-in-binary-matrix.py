class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        if grid[0][0]==1:
            return -1
        visit=set()
        q=deque()
        q.append([(0,0),1])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            [row,col],move=q.popleft()
            if row==ROW-1 and col==COL-1:
                return move
            if row+1<ROW and col+1<COL and grid[row+1][col+1]==0 and (row+1,col+1) not in visit:
                q.append([(row+1,col+1),move+1])  
                visit.add((row+1,col+1)) 
            if 0<=row-1 and 0<=col-1 and (row-1,col-1) not in visit and grid[row-1][col-1]==0:
                q.append([(row-1,col-1),move+1])
                visit.add((row-1,col-1))   
            if 0<=row-1 and col+1<COL and (row-1,col+1)not in visit and grid[row-1][col+1]==0:
                q.append([(row-1,col+1),move+1])
                visit.add((row-1,col+1))
            if row+1<ROW and 0<=col-1 and (row+1,col-1) not in visit and grid[row+1][col-1]==0:
                q.append([(row+1,col-1),move+1])
                visit.add((row+1,col-1))
            for dr,dc in directions:
                r,c=row+dr,col+dc
                if (r,c) not in visit and 0<=r<ROW and 0<=c<COL and grid[r][c]==0:
                    q.append([(r,c),move+1])
                    visit.add((r,c))
        return -1            

