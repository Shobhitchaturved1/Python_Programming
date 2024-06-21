class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans=0
        if minutes==len(customers):
            return sum(customers)    
        for x,y in zip(grumpy,customers):
            if x==0:
                ans+=y
        a=0
        for r in range(len(customers)-minutes+1):
            res=0
            for j in range(r,r+minutes):
                if grumpy[j]==1:
                    res+=customers[j]
            a=max(a,res)
        return ans+a            

