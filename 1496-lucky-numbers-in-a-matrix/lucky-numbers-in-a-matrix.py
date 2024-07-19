class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROW,COL=len(matrix),len(matrix[0])
        def minrow(ind):
            minval=float("inf")
            ans=COL
            for i in range(COL):
                if matrix[ind][i]<minval:
                    minval=matrix[ind][i]
                    ans=i       
            return minval
        def maxcol(ind):
            maxval=float("-inf")
            ans=ROW
            for i in range(ROW):
                if matrix[i][ind]>maxval:
                    maxval=matrix[i][ind]     
            return maxval            
        for i in range(ROW):
            for j in range(COL):
                if minrow(i)==maxcol(j):
                    return [matrix[i][j]]