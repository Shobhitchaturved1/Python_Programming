class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix=[]
        suffix=[]
        pre=0 
        for i in nums:
            pre+=i
            prefix.append(pre)
        suf=0
        for i in reversed(nums):
            suf+=i
            suffix.append(suf)
        ans=0
        suffix=suffix[::-1]
        for i in range(len(nums)-1):
            if prefix[i]>=suffix[i+1]:
                ans+=1
        return ans                