class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        res=0
        freq=defaultdict(int)
        if k>len(nums):
            return 0
        l=0    
        for r in range(len(nums)):
            freq[nums[r]]+=1
            ans+=nums[r]
            if freq[nums[r]]>1:
                while freq[nums[r]]>1:
                    freq[nums[l]]-=1
                    ans-=nums[l]
                    l+=1
            
            if r-l+1>k:
                ans-=nums[l]
                freq[nums[l]]-=1
                l+=1
            if r-l+1==k:
                res=max(ans,res)    
        return res                    
