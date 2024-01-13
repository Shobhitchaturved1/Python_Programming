class Solution:
    def climbStairs(self, n: int) -> int:
        n1=1
        n2=2
        if n<=2:
            return n
        ans=0    
        while n>2:
            ans=n1+n2
            n1=n2
            n2=ans
            n-=1
        return ans    