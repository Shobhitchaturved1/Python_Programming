class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROW,COL=len(mat),len(mat[0])
        hashmap=defaultdict(int)
        for i,x in enumerate(arr):
            hashmap[x]=i
        ans=float("inf")
        for row in mat:
            res=float("-inf")
            for r in row:            
                res=max(res,hashmap[r])
            ans=min(ans,res)
        for col in range(COL):  
            res=float("-inf")  
            for row in range(ROW):
                res=max(res,hashmap[mat[row][col]])
            ans=min(ans,res)
        return ans                 