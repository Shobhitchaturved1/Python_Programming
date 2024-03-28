class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=0
        i=0
        j=0
        res=0
        hash_map=defaultdict(int)
        while i<len(nums) and j<len(nums):
            hash_map[nums[j]]+=1
            if hash_map[nums[j]]<=k:
                ans+=1
            else:
                res=max(res,ans)
                while hash_map[nums[j]]>k:
                    hash_map[nums[i]]-=1
                    i+=1
                ans=j-i+1
            j+=1
        return max(res,ans)            