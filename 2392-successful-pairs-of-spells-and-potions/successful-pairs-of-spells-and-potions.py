class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res=[]
        potions.sort()
        def bs(num):
            l=0
            r=len(potions)-1
            ans=0
            while l<=r:
                mid=(l+r)//2
                if potions[mid]*num>=success:
                    ans=len(potions)-mid
                    r=mid-1
                else:
                    l=mid+1
            return ans 

        for i in spells:
            res.append(bs(i))
        return res