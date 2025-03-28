class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            newdp=set()
            for t in dp:
                if t==target or t+nums[i]==target:
                    return True
                newdp.add(t)
                newdp.add(t+nums[i]) 
            dp=newdp
        return False           