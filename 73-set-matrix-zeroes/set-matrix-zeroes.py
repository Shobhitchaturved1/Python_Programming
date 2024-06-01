class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col=len(matrix),len(matrix[0])
        rows,cols=[],[]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        for i in range(row):
            for j in range(col):            
                if i in rows:
                    matrix[i][j]=0
                if j in cols:
                    matrix[i][j]=0    