class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            a=abs(i)
            if nums[a-1]<0:
                res.append(a)
            nums[a-1]=-nums[a-1] 
        return res       