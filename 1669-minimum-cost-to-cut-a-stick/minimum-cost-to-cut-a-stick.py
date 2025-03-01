class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.append(0)
        cuts.sort()
        dp={}
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>j:
                return 0
            mini=float("inf")
            for idx in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+solve(i,idx-1)+solve(idx+1,j)    
                mini=min(mini,cost)
            dp[(i,j)]=mini    
            return mini    
        return solve(1,len(cuts)-2)    