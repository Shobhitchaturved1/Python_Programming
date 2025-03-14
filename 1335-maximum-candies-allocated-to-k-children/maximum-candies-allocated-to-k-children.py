class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        ans=0
        def bs(i):
            count=0
            if i==0:return True
            for n in candies:
                count+=n//i
            return count>=k    
        while l<=r:
            mid=(l+r)//2
            if bs(mid):
                ans=max(ans,mid)
                l=mid+1
            else:
                r=mid-1    
        return ans            