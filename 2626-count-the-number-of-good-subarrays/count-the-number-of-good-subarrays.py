class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count=0
        hashmap=defaultdict(int)
        l=0
        for r in range(len(nums)):
            hashmap[nums[r]]+=1
            if hashmap[nums[r]]>=2:
                k-=(hashmap[nums[r]]-1)
                while k<=0 and l<=r:
                    if hashmap[nums[l]]>=2:
                        k+=(hashmap[nums[l]]-1)
                    hashmap[nums[l]]-=1
                    l+=1
                    count+=1+(len(nums)-r-1)
        return count            