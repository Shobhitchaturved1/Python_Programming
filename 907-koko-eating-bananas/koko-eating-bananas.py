class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def caneat(n):
            count=0
            for i in piles:
                count+=math.ceil(i/n)
            return count<=h    
        a,b=1,max(piles)
        ans=h
        while a<=b:
            mid=(a+b)//2
            if caneat(mid):
                ans=mid
                b=mid-1
            else:
                a=mid+1
        return ans                