class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        nums=[i for i in sorted(set(nums))]
        ear1,earn2=0,0
        for i in range(len(nums)):
            curEarn=hashmap[nums[i]]*nums[i]
            if i>0 and nums[i]==nums[i-1]+1:
                tmp=earn2
                earn2=max(earn2,earn1+curEarn)
                earn1=tmp
            else:
                tmp=earn2
                earn2+=curEarn
                earn1=tmp
        return earn2            

