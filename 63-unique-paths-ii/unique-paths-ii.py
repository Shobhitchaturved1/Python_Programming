class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        row=[0]*n
        row[n-1]=1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j]==1:
                    row[j]=0
                elif j+1<n:    
                    row[j]=row[j]+row[j+1]       
            #print(row)
        return row[0]            