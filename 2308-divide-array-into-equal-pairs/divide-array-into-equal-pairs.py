class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap=defaultdict(int)
        pair=len(nums)//2
        count=0
        for i in nums:
            hashmap[i]+=1
            if hashmap[i]==2:
                count+=1
                hashmap[i]=0
        return count==pair        
                