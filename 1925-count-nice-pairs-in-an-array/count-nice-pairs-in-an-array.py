class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count=0
        hash_map=defaultdict(int)
        for i in nums:
            num=i-int(str(i)[::-1])
            hash_map[num]+=1

        for i in hash_map:
            i=hash_map[i]
            #print(i)
            count+=(i*(i-1))//2
        return count%(10**9+7)       