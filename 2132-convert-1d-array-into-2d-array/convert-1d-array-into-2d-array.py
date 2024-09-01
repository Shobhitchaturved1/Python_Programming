class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)>m*n:
            return []
        ans=[]
        i=0
        for j in range(m):
            cur=[]
            for k in range(n):
                if i>=len(original):return []
                cur.append(original[i])
                i+=1               
            ans.append(cur)
        return ans            