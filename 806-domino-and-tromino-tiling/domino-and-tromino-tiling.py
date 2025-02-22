class Solution:
    def numTilings(self, n: int) -> int:
        if n<=2:
            return n
        ans=[0]*(n+1)
        ans[1]=1
        ans[2]=2
        ans[3]=5
        for i in range(4,n+1):
            ans[i]=(2*ans[i-1]+ans[i-3])%(10**9+7)
        return ans[n]    