class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        row=[]
        a=0
        for i in reversed(grid[-1]):
            a+=i
            row.append(a)
        row=row[::-1]
        for i in reversed(range(m-1)):
            for j in reversed(range(n)):
                if j+1<n:
                    row[j]=grid[i][j]+min(row[j],row[j+1])
                else:
                    row[j]+=grid[i][j]
        return row[0]                    