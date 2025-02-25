class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res=0
        curr=0
        odd=0
        even=0
        for i in arr:
            curr+=i
            if curr%2:
                res+=1+even
                odd+=1
            else:
                res+=odd
                even+=1        
        return res%(10**9+7)            