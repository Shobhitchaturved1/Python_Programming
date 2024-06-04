class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        cols=set()
        pos_diag=set()
        neg_diag=set()

        def backtrack(i):
            nonlocal ans
            if i==n:
                ans+=1
                return
            for j in range(n):
                if j in cols or (i+j) in pos_diag or (i-j) in neg_diag:
                    continue

                cols.add(j)
                pos_diag.add(i+j)
                neg_diag.add(i-j)

                backtrack(i+1)

                cols.remove(j)
                pos_diag.remove(i+j)
                neg_diag.remove(i-j)
        
        backtrack(0)
        return ans                    