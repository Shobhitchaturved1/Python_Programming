class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        high=int(c**(1/2))+1
        for i in range(high):
            b=sqrt(c-i*i)
            if b==int(b):
                return True    
        return False        