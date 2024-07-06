class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=set()
        if sum(nums)%2:
            return False
        dp.add(0)    
        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            newdp=set()
            for t in dp:
                if t==target or t+nums[i]==target:
                    return True
                newdp.add(t)
                newdp.add(t+nums[i])
            dp=newdp
        return False            