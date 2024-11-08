class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix=[nums[0]]
        pre=nums[0]
        hashmap=defaultdict(int)
        for i in range(1,len(nums)):
            pre=pre^nums[i]
            prefix.append(pre)
        maxi=2**maximumBit -1
        ans=[]
        for i in prefix:
            ans.append(i^maxi)
        return ans[::-1]            