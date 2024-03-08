class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map=defaultdict(int)
        maxi=0
        ans=0
        for i in nums:
            hash_map[i]+=1
            maxi=max(maxi,hash_map[i])
        for i in hash_map:    
            if hash_map[i]==maxi:
                ans+=maxi
        return ans        