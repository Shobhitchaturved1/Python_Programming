class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS,COLS=len(rowSum),len(colSum)
        res=[[0]*COLS for i in range(ROWS)]
        for r in range(ROWS):
            res[r][0]=rowSum[r]
        for c in range(COLS):
            col_sum=0
            for r in range(ROWS):
                col_sum+=res[r][c] 
            r=0
            while col_sum>colSum[c]:
                diff=col_sum-colSum[c]
                max_shift=min(diff,res[r][c])
                res[r][c]-=max_shift
                res[r][c+1]=max_shift
                col_sum-=max_shift
                r+=1
        return res        
