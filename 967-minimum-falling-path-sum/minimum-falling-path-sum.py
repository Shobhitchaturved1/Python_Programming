class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        col=len(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(col):
                if j+1<col and j-1>=0:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1],matrix[i-1][j-1])
                elif j-1<0:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                else:
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j])
            #print(row)        
        return min(matrix[-1])                    