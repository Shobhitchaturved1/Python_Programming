class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        positivediag=set()
        negativediag=set()
        res=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in positivediag or (r-c) in negativediag:
                    continue
                col.add(c)
                positivediag.add(r+c)
                negativediag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                positivediag.remove(r+c)
                negativediag.remove(r-c)
                board[r][c]="."        
        backtrack(0)
        return res        