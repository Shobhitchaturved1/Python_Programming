class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res=0
        neg_count=0
        min_val=float("inf")
        for row in matrix:
            for n in row:
                res+=abs(n)
                min_val=min(min_val,abs(n))
                if n<0:
                    neg_count+=1
        if neg_count%2:
            res-=2*min_val
        return res                