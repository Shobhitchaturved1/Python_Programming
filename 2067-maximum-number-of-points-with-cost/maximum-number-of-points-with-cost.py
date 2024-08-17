class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROW,COL=len(points),len(points[0])
        row=points[0]
        for r in range(1,ROW):
            next_row=points[r]
            left,right=[0]*COL,[0]*COL
            left[0]=row[0]
            for j in range(1,COL):
                left[j]=max(row[j],left[j-1]-1)
            right[-1]=row[-1]    
            for j in range(COL-2,-1,-1):
                right[j]=max(row[j],right[j+1]-1)    
            for c in range(COL):
                next_row[c]+=max(left[c],right[c])
            row=next_row
        return max(row)                