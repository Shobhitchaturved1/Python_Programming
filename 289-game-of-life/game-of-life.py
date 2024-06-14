class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROW,COL=len(board),len(board[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        change=set()
        def checklive(r,c):
            count=0
            for dr,dc in directions:
                row,col=r+dr,c+dc
                if (0<=row<ROW and 0<=col<COL and board[row][col]==1):
                    count+=1
            if board[r][c]==0: 
                if count==3:
                    change.add((r,c))
                    return
                else:
                    return     
            if count<2 or count>3:
                change.add((r,c))
                return            
            return 

        for r in range(ROW):
            for c in range(COL):
                checklive(r,c)  
        print(change)        
        for r,c in change:
            if board[r][c]:
                board[r][c]=0
            else:
                board[r][c]=1               
        