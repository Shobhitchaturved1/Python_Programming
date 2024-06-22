class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        numdict=defaultdict(int)
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,num):
            nonlocal a
            grid[r][c]=num
            for dr,dc in directions:
                row,col=r+dr,c+dc
                if(0<=row<ROW and 0<=col<COL 
                   and grid[row][col]==1):
                   a+=1
                   dfs(row,col,num)
            return a       
        num=-1          
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    a=1
                    a=dfs(r,c,num)
                    numdict[num]=a
                    num-=1
        #print(grid)             
        finalans=0  
        #print(numdict)          
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    res=[]
                    for dr,dc in directions:
                        row,col=r+dr,c+dc
                        if(0<=row<ROW and 0<=col<COL):
                            res.append(grid[row][col])
                    #print(res)   
                    ans=0     
                    for x in set(res):
                        ans+=numdict[x]
                    finalans=max(ans+1,finalans)
        ans=finalans                                       
        if ans==0:
            return ROW*COL  
        return ans              
