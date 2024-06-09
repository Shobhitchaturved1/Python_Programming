class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        c,l=0,0
        for i in range(len(nums)):
            c=c+nums[i]
            r=c%k
            if r in d:
                l=l+d[r]
                d[r]+=1
            else:
                d[r]=1
        return l            