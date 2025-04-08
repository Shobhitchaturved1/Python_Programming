class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        hashmap=defaultdict(int)
        for i in range(len(nums)-1,-1,-1):             
            hashmap[nums[i]]+=1
            if hashmap[nums[i]]>1:
                break
        #print(i)        
        return math.ceil((i+1)/3) if hashmap[nums[i]]>1 else 0     