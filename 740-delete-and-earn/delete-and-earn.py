class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        res=[i for i in sorted(set(nums))]
        dp=[0]*len(res)
        dp[-1]=res[-1]*hashmap[res[-1]]
        for i in range(len(res)-2,-1,-1):
            if res[i+1]-1==res[i]:
                if i+2<len(res):
                    dp[i]=max(dp[i+1],res[i]*hashmap[res[i]]+dp[i+2])
                else:    
                    dp[i]=max(dp[i+1],res[i]*hashmap[res[i]])
            else:
                dp[i]=res[i]*hashmap[res[i]]+dp[i+1]     
        #print(dp)           
        return dp[0]        