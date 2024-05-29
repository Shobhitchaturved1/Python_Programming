class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])-1
        while top<bottom:
            if matrix[top][left]==target or matrix[top][right]==target:
                return True
            elif matrix[top][left]<target and target<matrix[top][right]:
                while left<=right:
                    mid=(right+left)//2
                    if matrix[top][mid]==target:
                        return True
                    elif matrix[top][mid]<target:
                        left=mid+1
                    else:
                        right=mid-1
                return False        
            else:
                top+=1
        return False                                