class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash_map=defaultdict(int)
        for i in nums:
            hash_map[i]+=1
        ans=0    
        for i in hash_map:    
            if hash_map[i]<=1:
                return -1
            j=hash_map[i]
            while j:
                if j>=3 and j!=4:
                    j-=3
                    ans+=1
                else:
                    j-=2
                    ans+=1
        return ans                