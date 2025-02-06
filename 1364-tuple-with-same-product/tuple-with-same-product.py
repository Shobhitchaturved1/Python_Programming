class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count=0
        hashmap=defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                hashmap[nums[i]*nums[j]]+=1
        for i in  hashmap.values():
            count+=8*(((i-1)*i)//2)
        return count            