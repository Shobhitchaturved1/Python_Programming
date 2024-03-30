class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans=0
        hash_map=defaultdict(int)
        near=0
        far=0
        for r in range(len(nums)):
            hash_map[nums[r]]+=1
            while len(hash_map)>k:
                hash_map[nums[near]]-=1
                if hash_map[nums[near]]==0:
                    hash_map.pop(nums[near])
                near+=1
                far=near    
            while hash_map[nums[near]]>1:
                hash_map[nums[near]]-=1
                near+=1    
            if len(hash_map)==k:
                ans+=near-far+1    
        return ans                   