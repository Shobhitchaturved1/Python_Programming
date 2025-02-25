class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=set()
        if sum(nums)%2:return False
        target=sum(nums)//2
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            newdp=set()
            for j in dp:
                if j==target or j+nums[i]==target:
                    return True
                newdp.add(j)
                newdp.add(j+nums[i])
            dp=newdp
        return False
