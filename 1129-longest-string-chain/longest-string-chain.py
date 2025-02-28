class Solution:
    def longestStrChain(self, nums: List[str]) -> int:
        nums.sort(key=len)
        dp=[1]*len(nums)
        maxi=1
        def check(s1,s2):
            if (len(s2)-len(s1))!=1:
                return False
            x,y=0,0
            while x<len(s1) and y<len(s2):
                if s1[x]==s2[y]:
                    x+=1
                    y+=1
                else:
                    y+=1
            return x==len(s1)           
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if check(nums[i],nums[j]) and dp[i]<1+dp[j]:
                    dp[i]=1+dp[j]
            if maxi<dp[i]:
                maxi=dp[i]
        return maxi                