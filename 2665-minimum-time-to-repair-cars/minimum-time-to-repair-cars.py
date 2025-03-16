class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l=min(ranks)
        r=max(ranks)*cars*cars
        ans=r
        def check(n):
            count=0
            for i in ranks:
                count+=math.floor(math.sqrt(n/i))
            return count>=cars    
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans            