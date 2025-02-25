class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(i,a):
            if (i,a) in dp:
                return dp[(i,a)]
            if i==len(nums):
                if a==target:
                    return 1
                return 0
            dp[(i,a)]=dfs(i+1,a+nums[i])+dfs(i+1,a-nums[i]) 
            return  dp[(i,a)]  
        return dfs(0,0)   