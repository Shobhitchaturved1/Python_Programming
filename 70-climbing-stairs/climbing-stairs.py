class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,0
        for i in range(n,-1,-1):
            tmp=one
            one=one+two
            two=tmp
        return two    
