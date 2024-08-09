class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        if ROW<3 or COL<3:return 0
        row=[[0,0],[0,1],[0,2]]
        col=[[0,0],[1,0],[2,0]]
        leftdiag=[[0,0],[1,1],[2,2]]
        rightdiag=[[0,2],[1,1],[2,0]]
        count=0
        def isduplicate(x,y):
            hashmap=defaultdict(int)
            for r in range(3):
                for c in range(3):
                    hashmap[grid[x+r][y+c]]+=1
                    if hashmap[grid[x+r][y+c]]>1 or 1>grid[x+r][y+c] or grid[x+r][y+c]>9:
                        return True
            return False            
        for i in range(ROW-2):
            for j in range(COL-2):
                if isduplicate(i,j):
                    continue
                r=c=ld=rd=0
                for dr,dc in row:
                    r+=grid[dr+i][dc+j]
                for dr,dc in col:
                    c+=grid[dr+i][dc+j]
                for dr,dc in leftdiag:
                    ld+=grid[dr+i][dc+j]
                for dr,dc in rightdiag:
                    rd+=grid[dr+i][dc+j]  
                if r==c==ld==rd:
                    count+=1
        return count                          
