class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix=[1]
        prefix=[1]
        a=1
        for i in nums:
            a=a*i
            suffix.append(a)
        a=1    
        for i in reversed(nums):  
            a=a*i
            prefix.append(a)
        #print(suffix)
        #print(prefix)
        res=[]
        j=len(prefix)-2
        i=0
        while j>0:
            res.append(prefix[j]*suffix[i])
            i+=1
            j-=1
        res.append(suffix[i])    
        return res      